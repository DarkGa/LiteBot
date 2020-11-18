import os
import shutil

class Main:
	
	version="1.0.0"
	info="Модуль для обновления бота, после обновления потребуется перезагрузка"
	group="System"
	
	async def init(app, m):
		
		os.system("rm -rf LiteBot; git clone https://github.com/DarkGa/LiteBot")
		files=[file for file in os.listdir("LiteBot") if file not in ["main.py", "config.ini"]]
		for file in files:
			if os.path.isfile(file): os.system(f"cp LiteBot/{file} {os.getcwd()}")
			else: os.system(f"cp -r LiteBot/{file} {os.getcwd()}")
		os.system("rm -rf LiteBot")
		
		await m.edit("**Бот был обновлен, требуется перезапуск!**")