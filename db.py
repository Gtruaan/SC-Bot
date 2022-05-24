import sqlite3

def get_users(*args):
    '''(optional) receives user ids to search as positional arguments and returns info in that order'''
   
    con = sqlite3.connect('swordcombat.db')
    cur = con.cursor()

    if args:
        users = []
        for user_id in args:
            cur.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
            users.append(cur.fetchall())
        return users

    cur.execute("SELECT * FROM users")
    return cur.fetchall()

def update_user(user_id, slot, new_spell_id):

    con = sqlite3.connect('swordcombat.db')
    cur = con.cursor()

    if get_users(user_id)[0]:
        cur.execute(f'''UPDATE users
                        SET slot_{slot}=?
                        WHERE user_id=?''', (new_spell_id, user_id))
        con.commit()
        return

    cur.execute(''' INSERT INTO users(user_id,slot_1,slot_2,slot_3,slot_4)
              VALUES(?,0,0,0,0) ''', (user_id,))
    con.commit()
    cur.execute(f'''UPDATE users
                    SET slot_{slot}=? 
                    WHERE user_id=?''', (new_spell_id, user_id))
    con.commit()
    return