import sqlite3 as sql
db = sql.connect('./hat_data.db')
cursor = db.cursor()
new_hat = raw_input("What hat would you like to delete? ")

cursor.execute("DELETE FROM hat_list WHERE hat_name=?",(new_hat,))

db.commit()
cursor.close()
db.close()