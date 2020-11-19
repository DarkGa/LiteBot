import os
from core.utils import utils

class Main:
	
	version="1.0.0"
	info="Модуль для обновления бота, после обновления потребуется перезагрузка"
	group="System"
	
	async def init(app, m):
		
		utils.bash("rm -rf LiteBot; git clone https://github.com/DarkGa/LiteBot")
		files=[file for file in os.listdir("LiteBot") if file not in ["main.py", "config.ini"]]
		for file in files:
			if os.path.isfile(file): utils.bash(f"cp LiteBot/{file} {os.getcwd()}")
			else: utils.bash(f"cp -r LiteBot/{file} {os.getcwd()}")
		utils.bash("rm -rf LiteBot")
		
		await m.edit("**Бот был обновлен, требуется перезапуск!**")