import os

global buff_util
buff_util={}

class utils:
	class buffer:
		'''
A helper class for the storage and transmission of temporary data.
		'''
		def write(data: list):
			try: buff_util[data[0]]=data[1]
			except: raise KeyError("Bad data format")
		def read(data: str):
			try: return buff_util[data]
			except: raise KeyError(f"Data from '{data}' not found")
		def clear(data: str):
			try: return buff_util.pop([data])
			except: raise KeyError(f"Data from '{data}' not found")
	
	def bash(code: str):
		return os.popen(code).read()