from core.loader import *

class Main:
	
	version="1.0.0"
	info="Получение списка модулей и группировка их по группам"
	group="System"
	
	async def init(app, m):
		
		groups={"groups": []}
		
		for module in loader.modules():
			try: group=loader.load(module[1:]).Main.group
			except: group="Unknow"
			
			try: groups[group]=groups[group]+", "+module[1:]
			except: groups[group]=module[1:]; groups["groups"].append(group)

		list_groups=""
		
		for group in groups["groups"]:
			list_groups+=f"**• {group}:** "
			list_modules=groups[group].replace(",","").split()
			i=0
			for module in list_modules:
				if i==0: list_groups+=f"```{module}```"
				else: list_groups+=f",``` {module}```"
				i+=1
			list_groups+="\n"
		
		await m.edit(f'''
**Все ваши модули:**
Для справки о модуле воспользуйтесь командой ```.help <module>```
[группа]: [модули]

{list_groups}
			''')