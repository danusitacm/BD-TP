from faker import Faker
import random
n=100000
def insert_into_game_event(db_manager):
    values=[]
    query_last_event_id="select event_id from event ORDER BY event_id DESC LIMIT 1"
    last_id_event=db_manager.get_last_id_from_table(query_last_event_id)
    query_last_game_id="select game_id from game ORDER BY game_id DESC LIMIT 1"
    last_id_game=db_manager.get_last_id_from_table(query_last_game_id)  
    values.append((1,1,(round(random.uniform(0.03, 0.8), 1))))
    query="insert into game_event (event_id,game_id,discount) values (%s,%s,%s)"
    db_manager.execute_query(query, values)
