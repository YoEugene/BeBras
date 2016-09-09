#-*- coding: UTF-8 -*-
from bs4 import BeautifulSoup

for i in range(2,46):
	with open(str(i)+'.html', 'r') as file:
		soup = BeautifulSoup(file.read(), 'html.parser')
		soup.findAll("a", {"class": "btn btn-default long-button"})[0].string = '看 解 答'
		soup.findAll("input", {"class": "btn btn-primary long-button"})[0].extract()
		soup.findAll("a", {"class": "btn btn-default long-button"})[0]['href'] = "http://bebras.csie.ntnu.edu.tw/main/?page=try_ans&id=" + str(i)
	
	with open(str(i)+'.html', 'w') as file:
		file.write(str(soup))