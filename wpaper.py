import bs4
import requests
import re
from urllib.parse import urljoin

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





#belongs in for loop, writes each wallpaper to file with unique name
with open(name+'.jpg', 'wb') as handle:
	response = requests.get(baseurl+indexurl+name+'/1920x1200/download', stream=True)
	for block in response.iter_content(1024):
		if not block:
			break
		handle.write(block)
		