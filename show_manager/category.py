from show import Show

class Category:

	def __init__(self, name):
		self._name = name
		self._shows = []
	
	#should just add object
	def to_category_add(self, new_show):
		self._shows.append(new_show)
