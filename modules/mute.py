from time import time
from pyrogram.types import ChatPermissions

class Main:
	
	version="1.0.0"
	info='''
Модуль для мута пользователя, используйте .mute для вечно мута, либо .mute 1d/1h/1m для временного.
	'''
	group="Admins"
	
	async def init(app, m):
		
		if len(m.text)<=6:
			try: await app.restrict_chat_member(m.chat.id, m.reply_to_message.from_user.id, ChatPermissions()); await m.edit(f"**{m.reply_to_message.from_user.first_name} потерял возможность писать навсегда**")
			except Exception as e: await m.edit("**Не достаточно прав!**"); print(e)
		else:
			params=m.text.split()
			if "d" in params[1]:
				times=time()+int(params[1].replace("d", ""))*60*60*24
			elif "h" in params[1]:
				times=time()+int(params[1].replace("h", ""))*60*60
			elif "m" in params[1]:
				times=time()+int(params[1].replace("m", ""))*60
			try: await app.restrict_chat_member(m.chat.id, m.reply_to_message.from_user.id, ChatPermissions(), int(times)); await m.edit(f"**{m.reply_to_message.from_user.first_name} потерял возможность писать на {params[1]}**")
			except: await m.edit("**Не достаточно прав!**")
			
			