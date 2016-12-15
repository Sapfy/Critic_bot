# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('BD.db')

c = conn.cursor()

c.execute('''SELECT bla1 FROM tell
              ORDER BY RANDOM()
              LIMIT 1''')


#   Закрываем текущее соединение с БД
conn.close()