import sqlite3 as sql


def initDB():
    # Create the sqlite database
    conn = sql.connect('database.db')

    c = conn.cursor()

    # Reset and create input, patches and output tables
    conn.execute('DROP TABLE IF EXISTS input')
    conn.execute('DROP TABLE IF EXISTS output')
    conn.execute('DROP TABLE IF EXISTS patches')

    conn.execute('CREATE TABLE input('
                 'process_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                 'room_size VARCHAR,'
                 'coords VARCHAR,'
                 'instructions varchar)'
                 )
    conn.execute('CREATE TABLE output('
                 'process_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                 'coords VARCHAR,'
                 'patches_cleaned VARCHAR)'
                 )
    conn.execute('CREATE TABLE patches('
                 'patch_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                 'process_id INTEGER,'
                 'CONSTRAINT fk_patches'
                 '  FOREIGN KEY (process_id)'
                 '  REFERENCES input(process_id))'
                 )

    conn.close()


def insertInput(username, password):
    con = sql.connect("database.db")
    cur = con.cursor()
    # cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username, password))
    con.commit()
    con.close()


def insertInput(username, password):
    con = sql.connect("database.db")
    cur = con.cursor()
    # cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username, password))
    con.commit()
    con.close()


def receive():
    con = sql.connect("database.db")
    cur = con.cursor()
    # cur.execute("SELECT username, password FROM users")
    users = cur.fetchall()
    con.close()
    return users
