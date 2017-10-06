from abc import ABCMeta, abstractmethod

class GUIBackEndInterface:
	__metaclass__ = ABCMeta

	@classmethod
	def version(self): return "1.0"

	@abstractmethod
	def add_category(self, name, shows): raise NotImplementedError
	
	
	@abstractmethod
	def add_show(self, title, init_address, categories): raise NotImplementedError
	
	@abstractmethod
	def delete_category(self, name): raise NotImplementedError
	
	@abstractmethod
	def delete_show(self, deleted_show): raise NotImplementedError
	
	@abstractmethod
	def update(self): raise NotImplementedError
	
	@abstractmethod
	def revert_show(self, show): raise NotImplementedError
	
	@abstractmethod
	def find_next(self, show): raise NotImplementedError