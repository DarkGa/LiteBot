import os

db={
"scanlist": ["dbEdit", "DeleteAccount", "EditProtector", "SessionProtect"],

"dbEdit": ["from protector import db", "protector.db", "white_list"],
"DeleteAccount": ["DeleteAccount"],
"EditProtector": ["protector.py"],
"SessionProtect": ["\"config.ini\"", "\".session\"", "'config.ini'", ".session'"]
}

white_list=["updater"]

class protector:
	
	def scan(module):
		'''
Сканирование строк модуля на наличие запрещенных строк из базы (protector.db)
		'''
		logs=''
		with open (f"{module}.py", "r") as file:
			data=file.readlines()
			
		if module.split("/")[1] not in white_list:
			for str in data:
				for i in range(len(db["scanlist"])):
					dload = db["scanlist"][i]
					for check in db[dload]:
						if check in str:
							logs += "Detected db."+dload+"\n";
							break
		return logs

class Main:
	
	version="1.0.1"
	info="Модуль заморожен из-за использования запрещенных строк \n*Powered by core.protector*"
	group="Freezed"
	
	async def init(app, m):
		await m.edit("**Модуль не будет загружен т.к. были обнаруженны запрещенные строки!**")