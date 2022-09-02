import requests,os,bs4
url = 'https://apod.nasa.gov/apod/'
os.makedirs('nasa',exist_ok = True)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,"html.parser")

photo = soup.select('img')
if photo == []:
    print('no image found')
else:
    photoUrl = photo[0].get('src')
    print('downloading %s.....'%(photoUrl))
    res = requests.get('https://apod.nasa.gov/apod/'+photoUrl)
    res.raise_for_status()
    imageFile = open(os.path.join('nasa',os.path.basename(photoUrl)),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    print('finished!')
