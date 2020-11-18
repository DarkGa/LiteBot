class Main:
	
	version="1.0.0"
	info='''
Модуль для разблокировки пользователя в группах.
	'''
	group="Admins"
	
	async def init(app, m):
		
		try: user=await app.get_users([m.text[7:]])
		except: pass
		try: await app.unban_chat_member(m.chat.id, user[0]["id"]); await m.edit(f"**Участник** '{user[0]['first_name']}'** был разблокирован.**")
		except Exception as e: await m.edit("**Не достаточно прав!**"); print(e)