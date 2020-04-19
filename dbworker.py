import sqlite3
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
