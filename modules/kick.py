class Main:
	
	version="1.0.0"
	info='''
Модуль для исключения пользователя из группы.
	'''
	group="Admins"
	
	async def init(app, m):
		
		try: await app.kick_chat_member(m.chat.id, m.reply_to_message.from_user.id); await app.unban_chat_member(m.chat.id, m.reply_to_message.from_user.id); await m.edit(f"**Участник** '{m.reply_to_message.from_user.first_name}'** был исключен.**")
		except: await m.edit("**Не достаточно прав!**")