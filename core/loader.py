import os
import sys
import functools
import importlib
from core.protector import *

class loader:
	
	def dynamic_import(module):
		if len(protector.scan(module.replace(".", "/")))==0:
			return importlib.import_module(module)
		else: return importlib.import_module("core.protector")
 
	
	def modules():
		'''
Function for returning a list of modules (all).
		'''
		ct=0
		modules=os.listdir("modules")
		list_modules=[]
		for module in modules:
			if module[-3:]==".py": list_modules.append("."+module[:-3]); ct+=1
			else: pass
		return list(list_modules)
		
	def unload(module):
		'''
Unload module, when you call an extension, it still loads, this method is typically used to operate the module file.
		'''
		try: del sys.modules["modules."+module[1:]]
		except: pass
		
	def load(module):
		'''
The module loader, 
that requires the module name as an argument,
returns the class.
		'''
		return loader.dynamic_import("modules."+module)
		
	def reload(module):
		'''
Reloading modules,
that requires the module name as an argument.
		'''
		try: del sys.modules["modules."+module[1:]]
		except: pass
		loader.dynamic_import("modules."+module[1:])
		
	def init():
		'''
Preloading all modules
		'''
		logs=""
		for module in loader.modules():
			try: loader.load(module[1:]); logs+=f"'{module[1:]}' preloading - succesfull\n"
			except: logs+=f"'{module[1:]}' preloading - failed\n"
		print(logs)
		