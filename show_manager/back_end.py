from category import Category

class BackEnd:

	def __init__(self):
		self._category_list = []
		self._general = Category("General")
		self._new = Category("New")
		
		self._category_list.append(self._general)
		self._category_list.append(self._new)
		
		
if __name__ == "__main__":
	bend = BackEnd()