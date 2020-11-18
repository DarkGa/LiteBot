from core.loader import *
import importlib
import traceback
import sys
import os

class Main:
	
	version="1.0.0"
	info="Модуль для перезагрузки ваших модулей."
	group="System"
	
	async def init(app, m):
		logs=""
		os.chdir(os.getcwd())
		for module in loader.modules():
			try: loader.reload(module)
			except: logs+=f'**• Не удалось загрузить "```{module}```", лог импорта:** ```{traceback.format_exc()}```\n'
			
		if len(logs)==0: await m.edit("**Перезагрузка прошла успешно**")
		else: await m.edit(logs)