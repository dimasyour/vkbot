import sqlite3
from datetime import datetime
conn = sqlite3.connect("db.db")
print('БД подключена...')
c = conn.cursor()

def check_if_exists(user_id):
    c.execute("SELECT * FROM users WHERE user_id = %d" % user_id)
    result = c.fetchone()
    if result is None:
        return False
    return True


def register_new_user(user_id):
    c.execute("INSERT INTO user_info(user_id, user_wish, user_admin, user_group) VALUES (%d, 0, 0, 0)" % user_id)
    conn.commit()
    c.execute("INSERT INTO users(user_id, state) VALUES (%d, '')" % user_id)
    conn.commit()

def get_user_state(user_id):
    c.execute("SELECT state FROM users WHERE user_id = %d" % user_id)
    result = c.fetchone()
    return result[0]

def get_user_wish(user_id):
    c.execute("SELECT user_wish FROM user_info WHERE user_id = %d" % user_id)
    result = c.fetchone()
    return result[0]

def set_user_group(user_id, user_group):
    c.execute("UPDATE user_info SET user_group=? WHERE user_id=?", (user_group, user_id))
    conn.commit()

def get_user_group(user_id):
    c.execute("SELECT user_group FROM user_info WHERE user_id = %d" % user_id)
    result = c.fetchone()
    return result[0]

def get_admin_status(user_id):
    c.execute("SELECT user_admin FROM user_info WHERE user_id = %d" % user_id)
    result = c.fetchone()
    return result[0]

def set_user_wish(user_id, user_wish):
    c.execute("UPDATE user_info SET user_wish = %d WHERE user_id = %d" % (user_wish, user_id))
    conn.commit()

def add_new_ob(text):
    date_ob = datetime.strftime(datetime.now(), "%d-%m-%Y %H:%M")
    c.execute("INSERT INTO ob_table(date_ob, text_ob) VALUES ('%s','%s')" % (date_ob, text))
    conn.commit()

def get_last_ob():
    c.execute("SELECT text_ob,date_ob FROM ob_table WHERE id=(SELECT MAX(id) FROM ob_table)")
    rows = c.fetchall()
    for row in rows:
        return('❗Последнее объявление: '+row[0]+'\n\nДобавленно: '+row[1])
