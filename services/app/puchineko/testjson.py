import json
from requests_oauthlib import OAuth1Session
import keys
import pprint

twitter = OAuth1Session(keys.CK, keys.CS, keys.AT, keys.ATS)

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
params ={'count' : 1}
req = twitter.get(url, params = params)
timeline = json.loads(req.text)

pprint.pprint(timeline, width=80)
