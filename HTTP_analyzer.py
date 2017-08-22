import requests
import logging
import re
import sqlite3
import os
from bs4 import BeautifulSoup



class HTTPAnalyzer:
	
	def __init__(self):
		self.rand = 6
		
	def find_next_ep(self, url):
		#take url up to end of episode number and increment ep number
		broken_list = re.compile('(ep[i\W]+.*?)([1-9]+)', re.IGNORECASE).split(url)
		url_to_next =  broken_list[0] + broken_list[1] + str(int(broken_list[2]) + 1)
	
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
		#print(resp.text)
		"""http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
		html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
		encoding = html_encoding or http_encoding"""
		soup = BeautifulSoup(resp.content, "lxml")

		for link in soup.find_all('a', href=True):
			if re.match(url_to_next, link['href']):
				url_to_next = link['href']
				break;

		print(url_to_next)
		
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
	analyzer.find_next_ep("https://www.watchcartoononline.io/star-wars-forces-of-destiny-episode-1-sands-of-jakku")
	analyzer.history_scan()
	#print(path)