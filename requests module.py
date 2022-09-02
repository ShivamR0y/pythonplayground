import requests
res = requests.get('http://reddit.com')
res.raise_for_status()
