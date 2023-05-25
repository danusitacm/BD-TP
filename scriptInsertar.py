import psycopg2
try:
    connection = psycopg2.connect(user="postgres",
                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="steam2")
    cursor = connection.cursor()
    postgres_insert_query = """ INSERT INTO event (name, description ,star_date,end_date) VALUES (%s,%s,%s,%s)"""
    record_to_insert = ('Primavera','Llego la primavera tenemos descuentos desde 50% ','2023-5-28','2023-5-29')
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")

except (Exception , psycopg2.Error) as error:
    print("Failed to insert record into event table", error)
    print(error)
finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")