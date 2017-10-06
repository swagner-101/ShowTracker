from category import Category
from show import Show
from HTTP_analyzer import HTTPAnalyzer
from storage import Storage
from GUIs_interface import GUIBackEndInterface
import logging

class BackEnd(GUIBackEndInterface):

	def __init__(self):
		self._analyzer = HTTPAnalyzer()
		self._storage = Storage()
		self._category_list = dict()
		self._up_to_date = []
		self._category_list["New"] = Category("New")
		self._category_list["General"] = Category("General")
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
			for show in shows:
				self._category_list[name].to_category_add(show)
		else:
			print("Duplicate Category Name")

	# intial add show into general and selected categories
	# ensure no duplicate show names
	def add_show(self, title, init_address, categories):
	
		#set up initial stuff for show
		next_ep = self._analyzer.find_next_ep(init_address, "FORWARD")
		episode_num = self._analyzer.find_ep_num(init_address)
		season_num = self._analyzer.find_season_num(init_address)

		#add return for none value on search for error
		new_show = Show(title, init_address, episode_num, season_num, next_ep)
		new_show._addresses.append(new_show._curr_address)
		new_show._addresses.append(new_show._next_address)
		
		#add show to categories selected
		self._category_list["General"].to_category_add(new_show)
		for category in categories:
			self._category_list[category].to_category_add(new_show)
			
	#delete category all together
	def delete_category(self, name):
	
		if name != "General" and name != "New":
			del self._category_list[name] 
			
	def delete_show(self, deleted_show, category_recieved):
		
		#if in general remove show from all categories
		if category_recieved == "General":
			for category in self._category_list.keys():
				try:
					self._category_list[category]._shows.remove(deleted_show)
				except ValueError:
					pass
		#or else remove from just the specified category
		else:
			try:
				self._category_list[category_recieved]._shows.remove(deleted_show)
			except ValueError:
				pass
	
	def revert_show(self, show):
		curr_i = show._addresses.index(show._curr_address)
		show._next_address = show._curr_address
		
		if curr_i == 0:
			show._curr_address = self._analyzer.find_next_ep(show._next_address, "REVERSE")
			show._addresses.insert(0, show._curr_address)
		else:
			show._curr_address = show._addresses[curr_i-1]
			
		show._episode_num = self._analyzer.find_ep_num(show._curr_address)
		show._season_num = self._analyzer.find_season_num(show._curr_address)

			
	#find next show a replace the show in waiting and the currently displayed one
	def find_next(self, show):
	
		#first check if next video can be found
		if show._next_address != None:
			print(show._next_address)
			temp_to_check = self._analyzer.find_next_ep(show._next_address, "FORWARD")
			print(temp_to_check)
		else:
			temp_to_check = self._analyzer.find_next_ep(show._curr_address, "FORWARD")
			if temp_to_check is None:
				logging.info("Couldn't find next episode")
				return False
	
		#update show with new address
		if show._next_address != None:
			temp = show._next_address
			show._next_address = temp_to_check
			show._addresses.append(show._next_address)
			show._curr_address = temp
		else:
			show._curr_address = temp_to_check
			show._addresses.append(show._curr_address)
		
		#update episode number and season number if needed
		if show._season_num != self._analyzer.find_season_num(show._curr_address):
			show._season_num+=1
			show._episode_num=1
		else:
			show._episode_num+=1
		
		return True
		
if __name__ == "__main__":
	bend = BackEnd()
	
	bend.add_show("Adventure Time", "https://www.watchcartoononline.io/adventure-time-season-1-episode-1-slumber-party-panic", ["gggggg"])
	bend.add_show("Out There", "https://www.watchcartoononline.io/out-there-episode-2-quest-for-fantasy", ["gggggg"])
	#print(bend._category_list["General"]._shows[1]._curr_address)
	bend.find_next(bend._category_list["General"]._shows[1])
	print(bend._category_list["General"]._shows[1]._curr_address)
	bend.revert_show(bend._category_list["General"]._shows[1])
	print(bend._category_list["General"]._shows[1]._curr_address)
	
