from librerias import *

def insert_into_game(db_manager):
    values=[]
    num_records=600
    query_last_developer_id ="select developer_id from developer ORDER BY developer_id DESC LIMIT 1"
    last_developer_id=db_manager.get_last_id_from_table(query_last_developer_id)
    query_insert_game ="INSERT INTO game (description,name,release_date,base_price,developer_id) VALUES (%s,%s,%s,%s,%s)"
    
    for _ in range(num_records):
        description=fake.text(max_nb_chars=300)
        name=fake.word()
        release_date=fake.date_this_year()
        base_price=random.randint(70000, 1000000) 
        developer_id=random.randint(1,last_developer_id)
        values.append((description,name,release_date,base_price,developer_id))   
    
    db_manager.executemany_query(query_insert_game, values)
  
