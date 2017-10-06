class Show:

	def __init__(self, title, curr, episode_num, season_num, next):
		self._title = title
		self._episode_num = episode_num
		self._season_num = season_num
		self._addresses = []
		self._curr_address = curr
		self._next_address = next
		
	def __del__(self):
		return