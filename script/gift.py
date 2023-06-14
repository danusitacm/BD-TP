from faker import Faker
import random
fake = Faker()
def insert_into_gift(db_manager):
    n=10
    values=[]
    query="INSERT INTO gift (shipping_date,user_id,game_gift_id,community_gift_id) VALUES (%s,%s,%s,%s)"
    query_last_id_purchase="SELECT user_buy_game FROM user_buy_game ORDER BY user_buy_game DESC LIMIT 1"
    query_last_id_community="select community_id from community ORDER BY community_id DESC LIMIT 1"
    last_id_community=db_manager.get_last_id_from_table(query_last_id_community)
    last_id_purchase=db_manager.get_last_id_from_table(query_last_id_purchase)
    for _ in range(n):
        shipping_date=fake.date_this_year()
        community_gift_id=random.randint(1,last_id_community)
        id_purchase=random.randint(1,last_id_purchase)
        query_purchase = f"SELECT user_id, game_id FROM user_buy_game WHERE user_buy_game={id_purchase} LIMIT 1"
        purchase_data = db_manager.get_data(query_purchase)
        if purchase_data:
            print(purchase_data)
            user_id=purchase_data[0][0]
            game_gift_id= purchase_data[0][1]
            values.append((shipping_date,user_id,game_gift_id,community_gift_id))   
    db_manager.executemany_query(query, values)