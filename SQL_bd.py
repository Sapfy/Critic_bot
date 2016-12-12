import pypyodbc

mySQLServer = "LAPTOP-0N1QACJF\SQLSAPFY"
myDatabase = "test1"

connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=' + mySQLServer + ';'
                              'Database=' + myDatabase + ';')
#   добавляем курсор
cursor = connection.cursor()

mySQLQuery = ("""
                SELECT tell
                FROM bla1
                """)

cursor.execute(mySQLQuery)
resul = cursor.fetchall()

print(resul)

connection.close()
