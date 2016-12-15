import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('BD.db')

    cur = con.cursor()
    cur.execute('''SELECT bla1 FROM tell
              ORDER BY RANDOM()
              LIMIT 1''')

    data = cur.fetchone()

    print("%s" % data)

except ValueError:

    print("Error &s:" % e.args[0])
    sys.exit(1)

finally:

    if con:
        con.close()