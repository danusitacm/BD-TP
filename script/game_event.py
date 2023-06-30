from faker import Faker
import random
import time
random.seed(int(time.time()) ) 
def insert_into_game_event(db_manager):
    n=2000000
    values=[]
    query_last_game_id="select game_id from game ORDER BY game_id DESC LIMIT 1"
    last_id_game=db_manager.get_last_id_from_table(query_last_game_id)
    query="insert into game_event (event_id,game_id,discount) values (%s,%s,%s) ON CONFLICT DO NOTHING"
    for i in range(n):
        event_id=random.randint(1,100)
        game_id=random.randint(1,last_id_game)
        discount=round(random.uniform(0.03, 0.8), 1)
        values.append((event_id,game_id,discount))
    db_manager.executemany_query(query, values)
