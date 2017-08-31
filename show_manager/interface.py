from abc import ABCMeta, abstractmethod

class StorageAndAnalyzer:
	__metaclass__ = ABCMeta

	@classmethod
	def version(self): return "1.0"

	@abstractmethod
	def find_next_ep(self, url): raise NotImplementedError
	
	@abstractmethod
	def history_scan(self): raise NotImplementedError