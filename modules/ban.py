class Main:
	
	version="1.0.0"
	info='''
Модуль для блокировки пользователя в группах.
	'''
	group="Admins"
	
	async def init(app, m):
		
		try: await app.kick_chat_member(m.chat.id, m.reply_to_message.from_user.id); await m.edit(f"**Участник** '{m.reply_to_message.from_user.first_name}'** был заблокирован.**")
		except: await m.edit("**Не достаточно прав!**")