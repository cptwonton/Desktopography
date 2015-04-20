import bs4
import requests
import re
from urllib.parse import urljoin
import os

#list of url's to images
urllist = []


baseurl = 'http://desktopography.net'

#baseurl+indexurl+name = url to image
#indexurl and name belong in for loop
indexurl = '/exhibition/2014'
name = '/the_source_of_life'

#scraping
r = requests.get(baseurl)
soup = bs4.BeautifulSoup(r.text)
links = [link.get('href') for link in soup.find_all('a')]
partial_links = [l for l in links if l and 'exhibition' in l and len(l.split(r'/'))==3]
#removes duplicates
partial_links = set(partial_links)

#appends partial to base
partial2_links = [urljoin(baseurl,l) for l in partial_links]
partial2_links.sort()


#creates directories to save wallpapers
if(not os.path.exists(r"C:/Desktopography")):
	os.makedirs(r"C:/Desktopography")
for links in partial2_links:
	currentyear = links[37:]
	yeardir = r"C:/Desktopography/" + currentyear
	if(not os.path.exists(yeardir)):
		os.makedirs(yeardir)
	r = requests.get(links)
	soup = bs4.BeautifulSoup(r.text)
	image_links = [links.get('href') for links in soup.find_all('a')]
	image2_links = [l for l in image_links if l and currentyear in l and len(l.split(r'/'))==4]
	image3_links = [urljoin(baseurl,l) for l in image2_links]
	for i in image2_links:
		name = i[16:]
		with open(yeardir+name+'.jpg', 'wb') as handle:
			response = requests.get(links+name+'/1920x1200/download', stream=True)
			for block in response.iter_content(1024):
				if not block:
					break
				handle.write(block)
		
	


	
		

		
	


		