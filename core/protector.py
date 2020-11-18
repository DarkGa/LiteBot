import os

db={
"scanlist": ["dbEdit", "DeleteAccount", "EditProtector", "SessionProtect"],

"dbEdit": ["from protector import db", "protector.db"],
"DeleteAccount": ["DeleteAccount"],
"EditProtector": ["protector.py"],
"SessionProtect": ["\"config.ini\"", "\".session\"", "'config.ini'", ".session'"]
}

class protector:
	def scan(module):
		logs=''
		with open (f"{module}.py", "r") as file:
			data=file.readlines()
			
		for str in data:
			for i in range(len(db["scanlist"])):
				dload = db["scanlist"][i]
				for check in db[dload]:
					if check in str:
						logs += "Detected db."+dload+"\n";
						break
		return logs

class Main:
	async def init(app, m):
		await m.edit("**Модуль не будет загружен т.к. были обнаруженны запрещенные строки!**")