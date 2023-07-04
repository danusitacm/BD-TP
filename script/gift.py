from librerias import *
def insert_into_gift(db_manager):
    num_records=200000
    values_gift=[]
    values_community_user=[]
    query_insert_gift="INSERT INTO gift (shipping_date,user_id,game_gift_id,community_gift_id) VALUES (%s,%s,%s,%s)"
    query_last_id_purchase="SELECT user_buy_game FROM user_buy_game ORDER BY user_buy_game DESC LIMIT 1"
    query_last_id_community="select community_id from community ORDER BY community_id DESC LIMIT 1"
    last_community_id=db_manager.get_last_id_from_table(query_last_id_community)
    last_purchase_id=db_manager.get_last_id_from_table(query_last_id_purchase)
    query_insert_community_user="INSERT INTO comunnity_user(community_id, user_community_id) VALUES (%s,%s) ON CONFLICT DO NOTHING"
    
    for _ in range(num_records):
        shipping_date=fake.date_this_year()
        community_gift_id=random.randint(1,last_community_id)
        id_purchase=random.randint(1,last_purchase_id)
        query_purchase = f"SELECT user_id, game_id, purchase_date FROM user_buy_game WHERE user_buy_game={id_purchase} LIMIT 1"
        purchase_data = db_manager.get_data(query_purchase)
        if purchase_data:
            user_id=purchase_data[0][0]
            game_gift_id= purchase_data[0][1]
            shipping_date=purchase_data[0][2]
            values_gift.append((shipping_date,user_id,game_gift_id,community_gift_id))   
            values_community_user.append((community_gift_id, user_id))
    
    db_manager.executemany_query(query_insert_gift, values_gift)
    db_manager.executemany_query(query_insert_community_user, values_community_user)