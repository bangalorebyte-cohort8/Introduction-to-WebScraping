#!/usr/bin/env python3.6


from bs4 import BeautifulSoup
import requests
import csv

url = ("http://www.boxofficemojo.com/yearly/chart/?page=%d&view=releasedate&view2=domestic&yr=2016&p=.htm")
rows = []
list_ = []
def pagination():
	for i in range(1,9):
		full_url = url % i
		list_.append(full_url)
	return  


def soupify(x):
	for i in x:
		page = requests.get(i)
		html = page.content
		s = BeautifulSoup(html)
		table = s.find("table", attrs = {'cellpadding': '5'	})
		return 

def get_rows(soupify(x):
		for i in table.find_all('tr'):
			cells =[]
			for cell in i.find_all('td'):
				text = cell.text
				cells.append(text)
			rows.append(cells)	
		print(rows)
pagination()
get_rows(soupify(list_))


outfile = open("./boxoffice5.csv", "")
writer = csv.writer(outfile)
writer.writerows(rows)
	
	



