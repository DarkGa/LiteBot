import requests
from core.loader import *

class Main:
	
	version="1.0.2"
	info='''
Загрузчик модулей.
Поддерживает загрузку модуля из файла, ссылки а так же официального репозитория.

Доступны аргументы: [link] [name]|official [module]|list|[none]

[link] [name] - загрузка по ссылке и назначения имени
[none] - без аргумента но с ответом на сообщение содержащие модуль
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
				if len(params)!=1:
					r = requests.get(params[1])
					open("modules/"+params[2]+".py", "w").write(r.text)
					try: loader.load(params[2]); await m.edit("**Load succesfull**")
					except Exception as e: await m.edit("**Load failed!**"); print(e)
					try: loader.reload(params[2])
					except: pass
				
			except Exception as e: await m.edit(e)
			