from librerias import *
def insert_into_community(db_manager):
    num_records = 100
    values = []
    query_insert_community = "INSERT INTO community (name, description) VALUES (%s, %s)"
    
    for i in range(num_records):
        name = f"community {i}"
        description = fake.text(max_nb_chars=300)
        values.append((name,description))
    
    db_manager.executemany_query(query_insert_community,values)