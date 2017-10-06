import sqlite3
from interface import StorageAndAnalyzer


class Storage(StorageAndAnalyzer):

	def __init__(self):
			self.conn = sqlite3.connect(database.db)
			self.c = self.conn.cursor()
	
		print("hello")

	def initialize(self):
		return
	
	
if __name__ == "__main__":
	print("what")