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
                SELECT (какие выгребаются столбики через запятую вот)
                FROM (откуда вытаскиваем(таблица называется))
                ''')