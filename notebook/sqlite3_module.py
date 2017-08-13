# https://docs.python.jp/3/library/sqlite3.html

import sqlite3

path = ':memory:'
conn = sqlite3.connect(path)

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS items;")
c.execute('''CREATE TABLE items(
    id INTEGER PRIMARY KEY,
    name TEXT,
    value INTEGER)''')

c.execute("INSERT INTO items (name, value) VALUES (?, ?)", ('one', 100))
c.execute("INSERT INTO items (name, value) VALUES (?, ?)", ('two', 200))
c.execute("INSERT INTO items (name, value) VALUES (?, ?)", ('three', 300))

data = [('four', 400), ('five', 500), ('six', 600)]
c.executemany("INSERT INTO items (name, value) VALUES (?, ?)", data)

conn.commit()

c.execute("SELECT * FROM items")
print(c.fetchall())
# [(1, 'one', 100), (2, 'two', 200), (3, 'three', 300), (4, 'four', 400), (5, 'five', 500), (6, 'six', 600)]

c.execute("SELECT * FROM items WHERE id >= ?", (4, ))
print(c.fetchall())
# [(4, 'four', 400), (5, 'five', 500), (6, 'six', 600)]

conn.close()
