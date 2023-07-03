from faker import Faker
import random
from datetime import datetime, timedelta,date
n=200000
fake = Faker()
def insert_into_user_buy_game(db_manager):
    values=[]
    start_date=date(2023, 1, 1)
    query_last_user_id="select user_id from user_1 ORDER BY user_id DESC LIMIT 1"
    last_id_user=db_manager.get_last_id_from_table(query_last_user_id)
    query_last_item_id="select item_id from item ORDER BY item_id DESC LIMIT 1"
    last_id_item=db_manager.get_last_id_from_table(query_last_item_id)
    query="INSERT INTO item_transacction (user_seller_id,purchase_date, price, user_buyer_id, item_sell_id) VALUES (%s,%s,%s,%s,%s)"
    for _ in range(1000):
        for _ in range(100):
            price=random.randint(70000, 1000000) 
            purchase_date=start_date 
            item_sell_id=random.randint(1,last_id_item)
            user_seller_id=random.randint(1,last_id_user)
            user_buyer_id=1+random.randint(1,last_id_user)
            values.append((user_seller_id,purchase_date, price, user_buyer_id, item_sell_id))
        start_date = purchase_date + timedelta(days=random.randint(0,1))
    db_manager.executemany_query(query, values)