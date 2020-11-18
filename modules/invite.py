from pyrogram.raw import functions

class Main:
	
	version="1.0.0"
	info='''
Модуль для приглашения пользователя в группу.
	'''
	group="Admins"
	
	async def init(app, m):
		
		try: user=await app.get_users([m.text[8:]])
		except: pass
		
		try: await app.add_chat_members(m.chat.id, user[0]["id"]); await m.edit("**Успешно**")
		except Exception as e: await m.edit("**Пользователь не найден!**"); print(e)