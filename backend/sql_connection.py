import pymysql

__cnx = None


def get_sql_connection():
    global __cnx
    __cnx = pymysql.connect(user='root', password='Crevilla*14',
                                      host='127.0.0.1',
                                      database='gs')

    return __cnx