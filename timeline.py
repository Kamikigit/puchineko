import json
from requests_oauthlib import OAuth1Session
from flask import Flask, render_template
import keys

twitter = OAuth1Session(keys.CK, keys.CS, keys.AT, keys.ATS)

app = Flask(__name__)

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
params ={'count' : 10}
req = twitter.get(url, params = params)

@app.route('/')
def get_post():  # 1ツイごとにpostsリストに格納
    if req.status_code == 200:
        timeline = json.loads(req.text)
        posts = []
        for tweet in timeline:
            posts.append(tweet['user']['name']+'<br>' \
                        + tweet['text'] + '<br>' \
                        + tweet['created_at'] + '<br>')
        return render_template('index.html', posts=posts)
    else:
        return "ERROR: %d" % req.status_code       

if __name__=='__main__':
    app.run(host='192.168.33.11',debug=True)
