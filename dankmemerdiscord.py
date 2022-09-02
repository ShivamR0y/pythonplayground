import time,requests
print('started')
link = ""

names = []

header = {
   }
while True:
    requests.post(link,data = {'content': "pls beg"},headers = header)
    time.sleep(1)
    requests.post(link,data = {'content': "pls fish"},headers = header)
    time.sleep(14)
    requests.post(link,data = {'content': "pls hunt"},headers = header)
    time.sleep(14)
    requests.post(link,data = {'content': "pls dig"},headers = header)
    time.sleep(14)
