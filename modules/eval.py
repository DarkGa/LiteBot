import traceback
import sys
import os
from io import StringIO
from meval import meval

class Main:
	
	version="1.0.0"
	info="Выполнение python кода через модуль."
	group="Language"
	
	async def init(app, m):

		async def addargc():
			return {"m": m, "app": app, "reply": m.reply_to_message,
								"phone": m.from_user.phone_number}

		code=""
			
		if ".eval " in m.text: code=m.text[6:]
		else: code=m.text[5:]
		
		logs=''
		old_stdout = sys.stdout
		result = sys.stdout = StringIO()
		reply=m.reply_to_message
		try: await meval(code, globals(), **await addargc())
		except: logs=traceback.format_exc()
		sys.stdout = old_stdout
		
		if len(logs)==0:
			await m.edit(f'''**code**:
	
```{code}```
	
**result**:
	
```{result.getvalue()}```
''')

		else:
			await m.edit(f'''**code**:
	
```{code}```
	
**Traceback output**:
	
```{logs}```
''')