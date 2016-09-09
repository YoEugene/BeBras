#-*- coding: UTF-8 -*-
import requests
import urllib
from bs4 import BeautifulSoup

saved = []

while len(saved) != 45:
    r = requests.get('http://bebras.csie.ntnu.edu.tw/main/?page=try')

    soup = BeautifulSoup(r.text.encode("utf-8"), 'html.parser')
    prob_id = soup.find(id="subform").attrs['action'].replace("?page=try_ans&id=","")
    imgs = soup.findAll("img")

    if prob_id not in saved:
        for img in imgs:
            src = img.get('src').encode('ascii')
            url = 'http://bebras.csie.ntnu.edu.tw/main/' + src
            urllib.urlretrieve(url, src)
        saved.append(prob_id)
        with open(prob_id+'.html', 'w') as file:
            file.write(r.text.encode("utf-8"))

        print(prob_id)
