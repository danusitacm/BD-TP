from librerias import *

def insert_into_user_buy_game(db_manager):
    values=[]
    start_date=date(2023, 1, 1)
    query_last_user_id="select user_id from user_1 ORDER BY user_id DESC LIMIT 1"
    last_user_id=db_manager.get_last_id_from_table(query_last_user_id)
    query_last_game_id="select game_id from game ORDER BY game_id DESC LIMIT 1"
    last_game_id=db_manager.get_last_id_from_table(query_last_game_id)
    query_insert_user_buy_game="INSERT INTO user_buy_game (total_price,purchase_date,game_id,user_id) VALUES (%s,%s,%s,%s)"
    
    for _ in range(50000):
        for _ in range(100):
            total_price=random.randint(70000, 1000000) 
            purchase_date=start_date 
            game_id=random.randint(1,last_game_id)
            user_id=random.randint(1,last_user_id)
            values.append((total_price,purchase_date,game_id,user_id))
        start_date = purchase_date + timedelta(days=random.randint(0,1))
    
    db_manager.executemany_query(query_insert_user_buy_game, values)
    