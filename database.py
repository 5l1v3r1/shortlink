import sqlite3
db = sqlite3.connect("bot.db", check_same_thread=False)
db.execute("CREATE TABLE IF NOT EXISTS robot(user_id INTEGER UNIQUE NOT NULL, language TEXT NOT NULL)")


def check_user(user_id: int):
    try:
        db.execute("INSERT INTO robot(user_id, language) VALUES(?,?)", (user_id, "En"))
        return "New_User"
    except sqlite3.IntegrityError:
        return "Old_User"

def new_user(user_id: int, language: str):
    try:
        db.execute("INSERT INTO robot(user_id, language) VALUES(?,?)", (user_id, language))
        db.commit()
    except:
        pass

def check_lang(user_id: int):
    check = db.execute("SELECT language FROM robot WHERE user_id = ?", (user_id,))
    for checker in check:
        lang = checker[0]
    return lang
