class Main:
	
	version="1.0.0"
	info='''
Модуль для удаления нескольких сообщений.
	'''
	group="Admins"
	
	async def init(app, m):
		
		for i in range(int(m.text[8:])+1):
			await app.delete_messages(m.chat.id, m.message_id-i)