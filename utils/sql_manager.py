import output
import sqlite3
import csv

output.info(f"Starting: {__name__}")

class SQL:
	
	def __init__(self, database_name: str, database: str, *keys) -> None:
		
		self.conn = sqlite3.connect(database)
		self.cur = self.conn.cursor()
		self.placeholders = ', '.join(['?']*len(keys))


		self.values = ", ".join(keys)

		self.cur.execute(f"CREATE TABLE IF NOT EXISTS {database_name} ({self.values})")


		self.database_name = database_name
		self.database = database

	def output_rows(self) -> list[str]:
		self.cur.execute(f"SELECT * from {self.database_name}")
		rows = self.cur.fetchall()	
		return rows
		
	def add_item(self, *item_names: str) -> None:
		try:
			ins = f'INSERT INTO {self.database_name} ({self.values}) VALUES({self.placeholders})'
			self.cur.execute(ins, tuple(i for i in item_names))
			output_items = ", ".join(item_names)
			output.complete(f"({self.database_name}) Added: {output_items}")
			self.conn.commit()	
		except sqlite3.ProgrammingError as e:
			output.error(e)
		
	def delete_item(self, **item_name) -> None:
		try:
			for key, value in item_name.items():
				ins = f'DELETE FROM {self.database_name} WHERE {key} = ?'
				self.cur.execute(ins, (value,))
				output.complete(f"({self.database_name}) Removed all instances of: {key}={value}")
			self.conn.commit()
		except sqlite3.ProgrammingError as e:
			output.error(e)
		except sqlite3.OperationalError:
			output.error(e)

if __name__ == '__main__':
	sql = SQL('test', 'test.db', 'title', 'date', 'time')
	sql.delete_item(title='bob')
	myList = sql.output_rows()
	print(myList)

