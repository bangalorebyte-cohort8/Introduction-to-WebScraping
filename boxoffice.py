#!/usr/bin/env python3.6


from bs4 import BeautifulSoup
import requests
import re
import csv

url = ("http://www.boxofficemojo.com/yearly/chart/?page=%d&view=releasedate&view2=domestic&yr=2016&p=.htm")
rows = []
list_ = []
def pagination():
	for i in range(1,9):
		full_url = url % i
		list_.append(full_url)
	print(list_)
pagination()
"""
def soupify(x):
	for i in x:
		page = requests.get(i)
		html = page.content
		s = BeautifulSoup(html,"lxml")
		table = s.find("table", attrs = {'cellspacing': '1'})
		for i in table.find_all('tr'):
			cells =[]
			for cell in i.find_all('td'):
				text = cell.text
				cells.append(text)
			rows.append(cells)			
change_year()
soupify(list_)


outfile = open("./boxoffice2016.csv", "w")
writer = csv.writer(outfile)
writer.writerows(rows)
"""
	

# check to see if soupify works on a single url
# take it back to orignial, non-function form and see if still works"""

