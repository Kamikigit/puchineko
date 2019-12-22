from flask import (
    Flask, jsonify, send_from_directory, render_template
import json
import os
from requests_oauthlib import OAuth1Session
from puchineko import keys, hate

twitter = OAuth1Session(keys.CK, keys.CS, keys.AT, keys.ATS)

app = Flask(__name__)
app.config.from_object("puchineko.config.Config")

url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
params ={'count' : 20}
req = twitter.get(url, params = params)

@app.route('/')
def get_post():  # 1ツイごとにposts辞書に格納
    if req.status_code == 200:
        timeline = json.loads(req.text)
        posts_good = []
        posts_bad = []
        for tweet in timeline:
            dic_good = {}
            dic_bad = {}
            judge =  [i for i in hate.hate if i in tweet['text']]
            if len(judge) > 0:
                icon = tweet['user']['profile_image_url_https']
                dic_bad["icon"] = '<img src=\"' + icon + '\">'
                dic_bad["username"] = tweet['user']['name']   
                dic_bad["tweet"] = tweet['text'] 
                posts_bad.append(dic_bad)
            else:
                icon = tweet['user']['profile_image_url_https']
                dic_good["icon"] = '<img src=\"' + icon + '\">'
                dic_good["username"] = tweet['user']['name']   
                dic_good["tweet"] = tweet['text'] 
                posts_good.append(dic_good)
        return render_template('index.html', posts_good=posts_good, posts_bad=posts_bad)
    else:
        return "ERROR: %d" % req.status_code   

@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)