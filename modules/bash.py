from core.utils import utils
import traceback

class Main:
	
	version="1.0.0"
	info="Выполение баш кода с возвратом ответа."
	group="Console"
	
	async def init(app, m):
		if m.text[:7]==".bash ": code=m.text[7:]
		else: code=m.text[6:]
		try: await m.edit(f'''
**Code:**

{code}

**Result:**

{utils.bash(code)}
		''')
		except: await m.edit(f'''
**Code:**

{code}

**Result:**

pyrogram.errors.exceptions.bad_request_400.MessageTooLong: [400 MESSAGE_TOO_LONG]: The message text is over 4096 characters (caused by "messages.EditMessage")
		''')