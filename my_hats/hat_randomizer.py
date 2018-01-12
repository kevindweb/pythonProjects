from random import randint
import sqlite3 as sql
db = sql.connect('./hat_data.db')
cursor = db.cursor()
our_hats = []


def my_random_hat():
    global our_hats
    all_hats = []
    for used in our_hats:
        if used[1] == 0:
            all_hats.append(used[0])
    if len(all_hats) == 0:
        for thing in range(0, len(our_hats) - 1):
            update_hat(our_hats[thing][0],0)
        our_num = randint(0,len(our_hats) - 1)
        update_hat(our_hats[our_num][0], 1)
        return our_hats[our_num][0]
    else:
        our_num = randint(0,len(all_hats) - 1)
        update_hat(our_hats[our_num][0],1)
        return all_hats[our_num]


def update_hat(this_hat, used_or_not):
    cursor.execute("UPDATE hat_list SET hat_used=? WHERE hat_name=?",(used_or_not,this_hat,))
    db.commit()

cursor.execute("SELECT * FROM hat_list")
for row in cursor.fetchall():
    our_hats.append([row[0],row[1]])


print("Your hat for the day is: " + str(my_random_hat()))