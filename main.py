import os
from core.loader import *
from pyrogram import filters
import pyrogram
import asyncio

app=pyrogram.Client("LiteBot")

loader.init()

global my_id

with app:
	my_id=app.get_me()["id"]

@app.on_message(filters.me & filters.text)
async def main(self, m):
	if my_id==m.from_user.id:
		module=m.text.split()
		if module[0] in loader.modules():
			await loader.load(module[0][1:]).Main.init(app,m)


app.run()