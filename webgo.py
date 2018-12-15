from bs4 import BeautifulSoup as BS
from os import listdir, makedirs
from requests import get


def webgo(url):
    global _soup
    res = get(url)
    _soup = BS(res.text, 'html.parser')


def elems(element,error=True):
    elems = _soup.select(element)
    if elems:
        return elems
    else:
        if error:
            print(f'Error: {error}')
        else:
            pass


def elems_imgs(elems):
    imgs = []
    for i in elems:
        element = i['href']
        if element.lower().endswith('.jpg') or element.lower().endswith('.jpeg')\
          or element.lower().endswith('.gif') or element.lower().endswith('.png')\
          or element.lower().endswith('.webm') or element.lower().endswith('.gifv')\
          or element.lower().endswith('.giphy') or element.lower().endswith('.webp')\
          or element.lower().endswith('.mp4') or element.lower().endswith('.mpeg'):
            imgs.append('http:' + element)
    return imgs


def download(folder, elements):
    global cache
    makedirs(folder + '/',exist_ok=True)
    cache = listdir('./' + folder + '/')
    for element in elements:
        filename = element.split('/')[-1]
        if filename in cache:
            print('Image exists')
            continue
        else:
            cache.append(filename)
            imgUrl = element
            print(imgUrl)
            res = get(imgUrl)
            with open(folder + '/' + filename, 'wb') as f:
                f.write(res.content)
                print(element.split('/')[-1] + ' DOWNLOADED')
