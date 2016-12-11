import pypyodbc

mySQLServer = ""
myDatabase = ""

connection = pypyodbc.connect('Driver(SQL Server);'
                              'Server=' + mySQLServer +';'
                              'Database=' + myDatabase +';'
                              'uid=;'
                              'pwd=;')
#   добавляем курсор
curson = connection.cursor()

mySQLQuery = ('''
                SELECT (какие выгребаются столбики через запятую)
                FROM (откуда вытаскиваем(таблица называется))
                ''')