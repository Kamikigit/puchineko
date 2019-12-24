from flask import (
    Flask,
    jsonify,
    send_from_directory,
    render_template,
    request,
)
import json
import os
from requests_oauthlib import OAuth1Session
from puchineko import keys, hate
from puchineko.utils import text2link
import oseti

twitter = OAuth1Session(keys.CK, keys.CS, keys.AT, keys.ATS)

app = Flask(__name__)
app.config.from_object("puchineko.config.Config")

url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
params ={'count' : 20}
req = twitter.get(url, params = params)

@app.route('/')
def get_post():  # 1ツイごとにposts辞書に格納
    if req.status_code == 200:
        return render_template('index.html')
    else:
        return "ERROR: %d" % req.status_code   

@app.route("/api/search/", methods=["POST"])
def search():
    search_word = request.form["text_name"]
    url = "https://api.twitter.com/1.1/search/tweets.json"
    params = {
        'q': search_word,
        'count': 20,
        'lang':'ja',
        'result_type': 'mixed'
    }
    req = twitter.get(url, params=params)
    analyzer = oseti.Analyzer()
    
    if req.status_code == 200:
        timeline = json.loads(req.text)
        posts_good = []
        posts_bad = []
        for tweet in timeline["statuses"]:
            dic = {}
            icon = tweet['user']['profile_image_url_https']
            dic["icon"] = '<img src=\"' + icon + '\">'
            dic["username"] = tweet['user']['name']   
            dic["tweet"] = text2link(tweet['text'], tweet['entities']) 
            result = analyzer.analyze(dic["tweet"])
            point = 0
            if len(result) > 1:
                point = sum(result) / len(result)
            else:
                point = result[0]

            if point >= 0:
                posts_good.append(dic)
            else:
                posts_bad.append(dic)
        return render_template('search.html', posts_good=posts_good, posts_bad=posts_bad, search_word=search_word)
    else:
        return "ERROR: %d" % req.status_code


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)
