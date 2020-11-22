import os
from core.utils import utils
from core.loader import loader
from web.web_panel import web_run as web

class Main:
	
	version="1.0.0"
	info="Модуль для запуска веб панели бота."
	group="System"
	
	async def init(app, m):
		
		argc=m.text.split()
		
		try: status=utils.buffer.read("web_panel")
		except: utils.buffer.write(["web_panel", True]); web(app); status=False
		
		if status: await m.edit("**Веб панель уже запущена и доступна по аддресу 127.0.0.1:5000**")
		else: await m.edit("**Веб панель была запущена и доступна по аддресу 127.0.0.1:5000**")