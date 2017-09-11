from category import Category
from show import Show
from HTTP_analyzer import HTTPAnalyzer
from GUIs_interface import GUIBackEndInterface

class BackEnd(GUIBackEndInterface):

	def __init__(self):
		self._analyzer = HTTPAnalyzer()
		self._category_list = dict()
		self._category_list["General"] = Category("General")
		self._category_list["New"] = Category("New")
		self._category_list["fff"] = Category("fff")
		self._category_list["ggg"] = Category("ggg")
		self._category_list["gggh"] = Category("gggh")
		self._category_list["tttt"] = Category("New")
		self._category_list["gggggg"] = Category("fff")
		self._category_list["ring"] = Category("ggg")
		self._category_list["anime"] = Category("gggh")
		
		#boolean array for settings
		self._settings = []
	
	#ensure no duplicates
	#add new category with list of shows
	def add_category(self, name, shows):
		if name not in self._category_list.keys():
			self._category_list[name] = Category(name)
			print("hello")
		#for show in shows:
			#self._category_list[name].add_show
	
	#delete category all together
	def delete_category(self, name):
		if name is not General and name is not New:
			del self._category_list[name] 

	# intial add show into general and selected categories
	# ensure no duplicate show names
	def add_show(self, title, init_address, categories):
		new_show = Show(title, init_address)
		self._category_list["General"].to_category_add(new_show)
		for category in categories:
			self._category_list[category].to_category_add(new_show)
			
	def update(self):
		#run history scan and check if anything clicked since initial load
		#has had the next episode watched
		
		#then update shows next episode
		return None
		
	def find_next(self, show):
		show._next_address = self._analyzer.find_next_ep(show._next_address)
		print (show._next_address)##switch to return

	
		
if __name__ == "__main__":
	bend = BackEnd()
	cats =[]
	bend.add_show("starwars", "https://www.watchcartoononline.io/star-wars-forces-of-destiny-episode-1-sands-of-jakku", cats)
	for show in bend._category_list["General"]._shows:
		if show._title == "starwars":
			bend.find_next(show)
		