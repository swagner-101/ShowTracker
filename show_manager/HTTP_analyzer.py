import requests
import logging
import re
import sqlite3
import os
from bs4 import BeautifulSoup
from interface import StorageAndAnalyzer


class HTTPAnalyzer(StorageAndAnalyzer):
	
	def __init__(self):
		return
		
	def find_next_ep(self, url, direction):
		#take url up to end of episode number and increment ep number
		broken_list = re.compile('(.*//.*?)(/.*)(ep[i\W]+.*?)([1-9]+0?)', re.IGNORECASE).split(url)
		
		if direction == "FORWARD":
			add = 1
		else:
			add = -1
			
			
		url_to_next_base = broken_list[1] + broken_list[2] + \
		broken_list[3] + str(int(broken_list[4]) + add)
		url_to_next_no_base = broken_list[2] + broken_list[3] + str(int(broken_list[4]) + add)
		
		
		u_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
		accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
		al = 'en-US,en;q=0.8'
		ae = 'gzip, deflate, sdch'
		cc = 'max-age=0'
		conn = 'keep-alive'

		headers = {
			'User-Agent': u_agent,
			'Accept': accept,
			'Accept-Language': al,
			'Accept-Encoding': ae,
			'Cache-Control': cc,
			'Connection': conn,
		}
		
		resp = requests.get(url, headers= headers)
		soup = BeautifulSoup(resp.content, "lxml")

		#Check references from site for matching full address or address without website name
		url_to_next = None
		for link in soup.find_all('a', href=True):
			if re.match(url_to_next_base, link['href']):
				url_to_next = link['href']
				break;
			elif re.match(url_to_next_no_base, link['href']):
				url_to_next = broken_list[0]+ broken_list[1] + link['href']
				break;
				
				
		#search for next season if episode could not be found within season
		if url_to_next == None:
			broken_list = re.compile('(.*//.*?)(/.*)(se[a\W]+.*?)([0-9]+)(.*)(ep[i\W]+.*?)([1-9]+0?)', re.IGNORECASE).split(url)
				
			url_to_next_base =  broken_list[1] + broken_list[2]+ broken_list[3] + str(int(broken_list[4]) + add) +broken_list[5]\
			+ broken_list[6] + "1"
			url_to_next_no_base = broken_list[2]+ broken_list[3] + str(int(broken_list[4]) + add) +broken_list[5]\
			+ broken_list[6] + "1"
			
					
			for link in soup.find_all('a', href=True):
				if re.match(url_to_next_base, link['href']):
					url_to_next = link['href']
					break;
				elif re.match(url_to_next_no_base, link['href']):
					url_to_next = broken_list[0]+ broken_list[1] + link['href']
					break;
				
		return url_to_next
	
	def find_ep_num(self, url):
		broken_list = re.compile('(ep[i\W]+.*?)([0-9]+)', re.IGNORECASE).split(url)
		return int(broken_list[2])
		
	def find_season_num(self, url):
		broken_list = re.compile('(se[a\W]+.*?)([0-9]+)', re.IGNORECASE).split(url)

		if len(broken_list) > 1:
			return int(broken_list[2])
		else:
			return 1

	def history_scan(self):
		data_base = self.find_path()
		script_dir = os.path.dirname(__file__)
		print(script_dir)
		print(data_base)            
		con = sqlite3.connect(data_base) #Connect to the database
		c = con.cursor()
		c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name") #Change this to your prefered query
		print(c.fetchall())
		
	def find_path(self):
		User_profile = os.environ["HOME"]
		History_path = "/Users/scottwagner/Library/Application\ Support/Firefox/Profiles/oxi0ps92.default/places.sqlite"
		return History_path
		
		
if __name__ == "__main__":

	analyzer = HTTPAnalyzer();
	analyzer.find_next_ep("https://www.watchcartoononline.io/rick-and-morty-season-3-episode-7-the-ricklantis-mixup", "FORWARD")
	#analyzer.history_scan()
	#print(path)