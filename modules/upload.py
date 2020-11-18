from core.loader import *

class Main:
	
	version="1.0.0"
	info='''
Отправка модуля в чат
	'''
	group="System"
	
	async def init(app, m):
		
		module=m.text.split()
		try:
			if "."+module[1] in loader.modules():
				await app.send_document(m.chat.id, f"modules/{module[1]}.py")
				await m.edit(f"**Модуль** '```{module[1]}```' **успешно отправлен.**")
			else: await m.edit(f"**Модуль** '```{module[1]}```' **не обнаружен.")
		except Exception as e: await m.edit(f"**Для отправки модуля укажите его после команды .upload**"); print(e)