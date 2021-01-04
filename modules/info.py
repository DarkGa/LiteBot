from pyrogram.raw import functions
from core.utils import utils

class Main:
	
	version="1.0.0"
	info="Модуль для вывода информации о пользователе."
	group="Work"
	
	async def init(app, m):
		
		await m.delete()
		
		if m.reply_to_message: user=m.reply_to_message.from_user
		else: user=m.from_user
		
		try: await app.download_media(user.photo.big_file_id, file_name='tmp/user_photo.png'); photo=True
		except: photo=False
		
		user = await app.send(
			functions.users.GetFullUser(
				id=await app.resolve_peer(user.id)
			)
		)
		
		utils.bash("mkdir tmp")
		
		user={
		"first_name": user.user.first_name,
		"last_name": user.user.last_name,
		"about": user.about,
		"username": user.user.username,
		"id": user.user.id,
		"is_bot": user.user.bot
		}
		
		for key in user:
			if user[key] is None:  user[key]="*пусто*"
			if user[key] is True: user[key]="да"
			if user[key] is False: user[key]="нет"
		
		
		
		msg=f'''
**Имя:** ```{user["first_name"]}```
**Фамилия:** ```{user["last_name"]}```
**Инфо:** ```{user["about"]}```
**Юзернейм:** ```{user["username"]}```
**Айди:** ```{user["id"]}```
**Бот:** ```{user["is_bot"]}```
		'''
		
		if m.reply_to_message:
			if photo: await m.reply_photo("tmp/user_photo.png", caption=msg, reply_to_message_id=m.reply_to_message.message_id)
			else: await m.reply(msg, reply_to_message_id=m.reply_to_message.message_id)
		else:
			if photo: await app.send_photo(m.chat.id, "tmp/user_photo.png", caption=msg)
			else: await app.send_message(m.chat.id, msg)
		
		utils.bash("rm -rf tmp")
		
