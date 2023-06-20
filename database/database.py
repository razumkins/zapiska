import sqlite3


conn = sqlite3.connect('database/db')
cursor = conn.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY,
                   username TEXT,
                   chat_id INTEGER,
                   trial_vip INTEGER,
                   vip INTEGER,
                   vip_time INTEGER,
                   search TEXT,
                   second_search TEXT,
                   third_search TEXT
               )""")


cursor.execute("""CREATE TABLE IF NOT EXISTS websites (
                   id INTEGER PRIMARY KEY,
                   chat_id INTEGER,
                   website TEXT
               )""")


conn.commit()
conn.close()