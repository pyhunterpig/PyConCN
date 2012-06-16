#coding=utf-8
import urllib
from json import loads
import os

def refresh():
    url = "http://simplejsonp.nodester.com/bootswatch/"
    result = loads(urllib.urlopen(url).read())
    if result:
        for theme in result.get("themes", []):
            sourcecssurl = theme["css"]
            cssfilename = sourcecssurl.replace('http://bootswatch.com/','static/css/')
            dirpath = os.path.dirname(cssfilename)
            if not os.path.isdir(dirpath):
                os.makedirs(dirpath)
            urllib.urlretrieve(sourcecssurl,cssfilename)
            sourcecssurl = theme["css-min"]
            cssfilename = sourcecssurl.replace('http://bootswatch.com/','static/css/')
            urllib.urlretrieve(sourcecssurl,cssfilename)            


if __name__ == '__main__':
    refresh()