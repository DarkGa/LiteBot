import requests
from core.loader import *

class Main:
	
	version="1.0.1"
	info='''
Загрузчик модулей.
Поддерживает загрузку модуля из файла, ссылки а так же официального репозитория.

Доступны аргументы: [link] [name]|official [module]|list|[none]

[link] [name] - загрузка по ссылке и назначения имени
official [module] - загрузка модуля из официального репозитория
list - список официальных модулей
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
					if params[1]=="official":
						r = requests.get("https://raw.githubusercontent.com/DarkGa/LiteBot-officially-modules/main/"+params[2]+".py")
						if str(r)=="<Response [200]>":
							open("modules/"+params[2]+".py", "w").write(r.text)
							try: loader.load(params[2]); await m.edit("**Load succesfull**")
							except Exception as e: await m.edit("**Load failed!**"); print(e)
							try: loader.reload(params[2])
							except: pass
						else:
							await m.edit(f"**Модуль '{params[2]}' не найден на официальном источнике, воспользуйтесь командой ```.load list``` для получения списка модулей")
					
					elif params[1]=="list":
						r=requests.get("https://raw.githubusercontent.com/DarkGa/LiteBot-officially-modules/main/database")
						modules=""
						for module in r.text.split():
							modules+="**• "+module+"**\n"
						
						await m.edit(f'''**Список официальных модулей:**

{modules}''')
					
					
					else:
						r = requests.get(params[1])
						open("modules/"+params[2]+".py", "w").write(r.text)
						try: loader.load(params[2]); await m.edit("**Load succesfull**")
						except Exception as e: await m.edit("**Load failed!**"); print(e)
						try: loader.reload(params[2])
						except: pass
				
			except Exception as e: await m.edit(e)
			