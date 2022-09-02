import requests,bs4,webbrowser

url = 'https://www.reddit.com/r/memes/'

print('starting....')
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,"html.parser")
linkElems = soup.select('._2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax')

numOpen = min(5,len(linkElems))
print(numOpen)
for i in range (numOpen):
    webbrowser.open(linkElems[i].get('src'))
    print(linkElems[i].get('src'))
