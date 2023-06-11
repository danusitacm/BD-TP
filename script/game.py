from faker import Faker
import random
n=20
fake = Faker()
def insert_into_game(db_manager):
    values=[]
    query="select developer_id from developer ORDER BY developer_id DESC LIMIT 1"
    end_range=db_manager.get_last_id_from_table(query)
    query="INSERT INTO game (description,name,release_date,base_price,developer_id) VALUES (%s,%s,%s,%s,%s)"
    for _ in range(n):
        description=fake.text(max_nb_chars=300)
        name=fake.word()
        release_date=fake.date_this_year()
        base_price=random.randint(70000, 1000000) 
        developer_id=random.randint(1,end_range)
        values.append((description,name,release_date,base_price,developer_id))   
    db_manager.execute_query(query, values)
    
def insert_into_user_buy_game(db_manager):
    values=[]
    query_last_user_id="select user_id from user_1 ORDER BY user_id DESC LIMIT 1"
    query_last_game_id="select game_id from game ORDER BY game_id DESC LIMIT 1"
    query="INSERT INTO user_buy_game (total_price,purchase_date,game_id,user_id) VALUES (%s,%s,%s,%s)"
    for _ in range(n):
        total_price=0  #este tenemos que cambiar#
        purchase_date=fake.date_this_year()
        game_id=random.randint(1,db_manager.get_last_id_from_table(query_last_game_id))
        user_id=random.randint(1,db_manager.get_last_id_from_table(query_last_user_id))
        values.append((total_price,purchase_date,game_id,user_id))   
    db_manager.execute_query(query, values)