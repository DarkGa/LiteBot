from core.loader import *
import os

class Main:
	
	version="1.0.0"
	info="Удаления модуля"
	group="System"
	
	async def init(app, m):
		
		try:
			module=m.text.split()
			if "."+module[1] in loader.modules():
				loader.unload("."+module[1])
				os.remove(f"modules/{module[1]}.py")
				await m.edit(f"**Модуль** '```{module[1]}```' **успешно удален.**")
			else: await m.edit(f"**Модуль** '```{module[1]}```' **не обнаружен.")
		except Exception as e: await m.edit(f"**Для удаления модуля укажите его после команды .del**"); print(e)
		