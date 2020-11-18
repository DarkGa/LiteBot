from core.loader import *

class Main:
	
	version="1.0.0"
	info="Модуль для получения инфромации из других модулей."
	group="System"
	
	async def init(app, m):
		module=m.text.split()
		if len(module)!=1:
			if "."+module[1] in loader.modules():
				
				mot=loader.load(module[1]).Main
				
				info=""
				version=""
				
				try: version=mot.version
				except: version="Неизвестно"
				try: info=mot.info
				except: info="Неизвестно"
					
				await m.edit(f'''
**Название:** ```{module[1]}```
**Версия:** ```{version}```

**Информация:** ```{info}```''')

			else:
				await m.edit(f'''
**Модуль "{module[1]}" не найден.**
				''')

		else:
			await m.edit(f'''
**Модуль для получения инфромации из других модулей.**

**Пример использования:** ```.help test```
			''')