import requests

res = requests.get('http://inet-ip.info/ip')
print(res.text)
