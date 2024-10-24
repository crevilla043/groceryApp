import mysql.connector

cnx = mysql.connector.connect(user='root', password='Crevilla*14',
                              host='127.0.0.1',
                              database='gs')

cursor = cnx.cursor()
query = "SELECT * FROM gs.uom"

cursor.execute(query)

for (uom_id, uom_name) in cursor:
    print(uom_id, uom_name)


cnx.close()