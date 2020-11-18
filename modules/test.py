import os
import speedtest 
from datetime import datetime

class Main:
	
	version="1.0.0"
	info='''
Тестирование скорости ответа бота, пинг и скорость загрузки/отправки.
	'''
	group="System"
	
	async def init(app, m):
		
		s = speedtest.Speedtest()
		
		start = datetime.now()
		await m.edit("```Тестируем скорость работы...```")
		end = datetime.now()
		ms = (end - start).microseconds / 1000
		
		await m.edit("```Проверяем пинг...```")
		s.get_best_server()
		await m.edit("```Проверяем скорость загрузки...```")
		s.download()
		await m.edit("```Проверяем скорость отправки...```")
		s.upload()
		res=s.results.dict()
		await m.edit(f"**Задержка: {ms} ms**" \
								f"**\nПинг: {int(res['ping'])} ms**" \
								f"\n**Загрузка: {int(res['download']/1024/1024)} mib/s**" \
								f"\n**Отправка: {int(res['upload']/1024/1024)} mib/s**")