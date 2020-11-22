import os
import sqlite3

global buff_util
buff_util={}

class utils:
	class buffer:
		'''
A helper class for the storage and transmission of temporary data.
		'''
		def write(data: list):
			try: buff_util[data[0]]=data[1]
			except: raise KeyError("Bad data format")
		def read(data: str):
			try: return buff_util[data]
			except: raise KeyError(f"Data from '{data}' not found")
		def clear(data: str):
			try: return buff_util.pop([data])
			except: raise KeyError(f"Data from '{data}' not found")
	
	def bash(code: str):
		return os.popen(code).read()
		
	class db:
		
		def create_table(table: str, column: str):
			
			conn = sqlite3.connect("LiteBot.db")
			cursor = conn.cursor()
			cursor.execute(f"CREATE TABLE `{table}` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `{column}` INTEGER);")
			conn.commit()
			conn.close()
		
		def add_table(table: str, column: str):
			
			conn = sqlite3.connect("LiteBot.db")
			cursor = conn.cursor()
			cursor.execute(f"ALTER TABLE `{table}` ADD COLUMN `{column}` INTEGER;")
			conn.commit()
			conn.close()
		
		def insert_into(table: str, column: str, data):
			
			conn = sqlite3.connect("LiteBot.db")
			cursor = conn.cursor()
			cursor.execute(f"INSERT INTO `{table}` (`id`, `{column}`) VALUES (NULL, '{data}');")
			conn.commit()
			conn.close()
		
		def update(table: str, column: str, data):
			
			conn = sqlite3.connect("LiteBot.db")
			cursor = conn.cursor()
			cursor.execute(f"UPDATE `{table}` SET `{column}`='{data}'")
			conn.commit()
			conn.close()
			
		def drop_table(table: str):
			
			conn = sqlite3.connect("LiteBot.db")
			cursor = conn.cursor()
			cursor.execute(f"DROP TABLE {table};")
			conn.commit()
			conn.close()
			
		def select(table: str, column: str):
			
			conn = sqlite3.connect("LiteBot.db")
			cursor = conn.cursor()
			sql=f"SELECT `{column}` FROM `{table}`"
			cursor.execute(sql)
			post={}
			for i in cursor.fetchall():
				post=i
			return post