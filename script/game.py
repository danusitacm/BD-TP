from faker import Faker
import random
n=10
fake = Faker()
def insert_into_game(db_manager):
    values=[]
    start_range=1
    end_range=10
    query="INSERT INTO game (description,name,release_date,base_price,developer_id) VALUES (%s,%s,%s,%s,%s)"
    for _ in range(n):
        description=fake.text(max_nb_chars=300)
        name=fake.name()
        release_date=fake.date_this_year()
        base_price=fake.pydecimal(left_digits=3, right_digits=2, positive=True)
        developer_id=random.randint(start_range, end_range)
        values.append((description,name,release_date,base_price,developer_id))   
    db_manager.execute_query(query, values)
    
def insert_into_user_buy_game(db_manager):
    values=[]
    start_range=1
    end_range=10
    query="INSERT INTO user_buy_game (total_price,purchase_date,game_id,user_id) VALUES (%s,%s,%s,%s)"
    total_price=random.uniform(start_range,end_range)  #este tenemos que cambiar#
    purchase_date=fake.date_this_year()
    game_id=random.randint(start_range, end_range)
    user_id=random.randint(start_range, end_range)
    values.append((total_price,purchase_date,game_id,user_id))   
    db_manager.execute_query(query, values)