import requests
from core.loader import *

class Main:
	
	version="1.0.0"
	info='''
Загрузчик модулей.
Поддерживает загрузку модуля из файла и по ссылке.
	'''
	group="System"
	
	async def init(app, m):
		
		type=''
		
		if m.reply_to_message:
			try: m.reply_to_message.document; type="file"
			except: type="Unknown"
		else:
			type="text"
			
		if type=="file":
			await app.download_media(m.reply_to_message, file_name="modules/"+m.reply_to_message.document.file_name)
			try: loader.load(m.reply_to_message.document.file_name[:-3]); await m.edit("**Load succesfull**")
			except: await m.edit("**Load failed!**")
			try: loader.reload(m.reply_to_message.document.file_name[:-3])
			except: pass
			
		elif type=="text":
			try:
				params=m.text.split()
				r = requests.get(params[1])
				open(params[2], "w").write(r.text)
				try: loader.load(params[1]); await m.edit("**Load succesfull**")
				except: await m.edit("**Load failed!**")
				try: loader.reload(params[1])
				except: pass
			except Exception as e: await m.edit(e)
			