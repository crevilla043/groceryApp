from datetime import datetime

from sql_connection import get_sql_connection


def insert_order(connection, order):
    cursor = connection.cursor()
    order_query = ("INSERT INTO orders "
                   "(customer_name, total, datetime)"
                   "VALUES (%s, %s, %s)")
    order_data = (order['customer_name'], order['grand_total'], datetime.now())

    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid

    order_details_query = ("INSERT INTO orders "
                   "(customer_name, total, datetime)"
                   "VALUES (%s, %s, %s)")
    order_details_data = []
    for order_detail_record in order ['order_details'] :
        order_details_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            int(order_detail_record['total_price'])
        ])

    cursor.executemany(order_details_query, order_details_data)

    connection.commit()
    return order_id

if __name__=='__main__':
    connection = get_sql_connection()
    print(insert_order(connection, {
        'customer_name' : 'Judy',
        'total' : ' ',
        'order_details' : [
            {
                'product_id' : 2,
                'quantity' : 3,
                'total_price' : 25
            },
            {
                'product_id': 1,
                'quantity': 10,
                'total_price': 59.9
            }
        ]
    }))