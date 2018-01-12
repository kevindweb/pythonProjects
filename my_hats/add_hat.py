import sqlite3 as sql
db = sql.connect('./hat_data.db')
cursor = db.cursor()
new_hat = raw_input("What hat would you like to add? ")

cursor.execute("INSERT INTO hat_list (hat_name, hat_used) VALUES (?, ?)", (new_hat, 0))
db.commit()
cursor.close()
db.close()