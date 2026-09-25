import psycopg2
import csv

def table_from_csv(table_name, file_name):
    conn = psycopg2.connect(
        dbname = 'north',
        user = 'postgres',
        password = 'bblchara1',
        port = 5432,
        host = 'localhost'
    )

    cursor = conn.cursor()
    with open(file_name) as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        for row in csv_reader:
            query = f'Insert into {table_name.upper()} ({", ".join(header)}) values ({", ".join(["%s"] * len(row))})'
            cursor.execute(query, row)

    conn.commit()
    cursor.close()
    conn.close()

def main():
    table_from_csv('employee', 'data/employees_data.csv')
    table_from_csv('customers', 'data/customers_data.csv')
    table_from_csv('orders', 'data/orders_data.csv')



if __name__ == '__main__':
    main()