class Main:
	async def init(app, m):
		await app.send_message(m.chat.id, "config.ini")
