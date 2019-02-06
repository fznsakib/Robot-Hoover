import sqlite3 as sql


def initDB():
    # Create the sqlite database
    conn = sql.connect('database.db')

    # Reset and create input, patches and output tables
    conn.execute('DROP TABLE IF EXISTS input')
    conn.execute('DROP TABLE IF EXISTS output')
    conn.execute('DROP TABLE IF EXISTS patch')

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
    conn.execute('CREATE TABLE patch('
                 'patch_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                 'process_id INTEGER,'
                 'patch_coords VARCHAR,'
                 'CONSTRAINT fk_patches'
                 '  FOREIGN KEY (process_id)'
                 '  REFERENCES input(process_id))'
                 )

    conn.close()


def insertInput(roomSize, coords, patches, instructions):
    con = sql.connect("database.db")
    cur = con.cursor()

    # Insert into input table
    cur.execute('INSERT INTO input (room_size, coords, instructions) VALUES (?,?,?)',
                (str(roomSize).strip('[]'), str(coords).strip('[]'), str(instructions)))

    # Get current process id
    cur.execute('SELECT process_id FROM input ORDER BY process_id DESC LIMIT 1')
    processid = cur.fetchone()[0]

    # Insert patches into patch table
    for patch in patches:
        patch = str(patch).strip('[]')
        cur.execute('INSERT INTO patch (process_id, patch_coords) VALUES (?, ?)', (processid, patch))

    con.commit()
    con.close()


def insertOutput(coords, patchesCleaned):
    con = sql.connect("database.db")
    cur = con.cursor()

    # Insert into output table
    cur.execute("INSERT INTO output (coords, patches_cleaned) VALUES (?,?)", (str(coords).strip('[]'), patchesCleaned))

    con.commit()
    con.close()


def receiveTables():
    con = sql.connect("database.db")
    cur = con.cursor()

    # Get rows from every table
    cur.execute("SELECT * FROM input")
    input = cur.fetchall()

    cur.execute("SELECT * FROM patch")
    patch = cur.fetchall()

    cur.execute("SELECT * FROM output")
    output = cur.fetchall()
    con.close()

    return input, patch, output

