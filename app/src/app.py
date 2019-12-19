import json
import os
from requests_oauthlib import OAuth1Session
from flask import Flask, render_template
import keys
import hate

twitter = OAuth1Session(keys.CK, keys.CS, keys.AT, keys.ATS)

app = Flask(__name__)

url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
params ={'count' : 10}
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


if __name__=='__main__':
    app.run(host='192.168.33.11')
   #host='puchineko.com',debug=True)
    #163.215.6.1
