import sqlite3
from interface import StorageAndAnalyzer
from category import Category
from show import Show

class Storage(StorageAndAnalyzer):

	def __init__(self, categories, upto_date):
		self.conn = sqlite3.connect('database.db')
		self.c = self.conn.cursor()
		
		#initialize categories from DB
		for row in self.c.execute('SELECT * FROM Categories'):
			categories[row[0]] = Category(row[0])
		
		#initialize shows with all adresses and add to correspond categories
		for row in self.c.execute('SELECT * FROM Shows ORDER BY title'):
			new_show = Show(row[0], row[3], row[1], row[2], row[4])
			
			#add addresses related to show to addresses
			title_cat = (row[0],)
			for row2 in self.c.execute('SELECT * FROM addresses WHERE show = ?', title_cat):
				new_show._addresses.append(row2[0])
			
			#add show to any categories it is associated with including upto_date list
			for row3 in self.c.execute('SELECT * FROM Has WHERE show_name = ?', title_cat):
				if row3[0] == "upto_date":
					upto_date.append(new_show)
				else:
					categories[row3[0]].to_category_add(new_show)
	
	
		
	def close_DB(self, categories, upto_date):
		
		#clear tables
		self.c.execute('DELETE FROM addresses')
		self.c.execute('DELETE FROM Has')
		self.c.execute('DELETE FROM Categories')
		self.c.execute('DELETE FROM Shows')
		
		#store shows  and then the addresses regarding each show
		for show in categories["General"]._shows:
			show_tup = (show._title, show._episode_num, show._season_num, show._curr_address, show._next_address)
			self.c.execute("INSERT INTO Shows VALUES (?,?,?,?,?)", show_tup)
			
			for address in show._addresses:
				address_tup = (address, show._title)
				self.c.execute("INSERT INTO addresses VALUES (?,?)", address_tup)
		
		#store categories and the relation to any show within
		for category in categories.keys():
			cat_tup = (category,)
			self.c.execute("INSERT INTO Categories VALUES (?)", cat_tup)
			
			for show in categories[category]._shows:
				has_tup = (category, show._title)
				self.c.execute("INSERT INTO Has VALUES (?,?)", has_tup)

		#commit to database and close connection
		self.conn.commit()
		self.conn.close()
