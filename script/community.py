from librerias import *
def insert_into_community(db_manager):
    num_communities = 100000
    values = []
    query_insert_community = "INSERT INTO community (name, description) VALUES (%s, %s)"
    
    for _ in range(num_communities):
        name = fake.word()
        description = fake.text(max_nb_chars=300)
        values.append((name,description))
    
    db_manager.executemany_query(query_insert_community,values)