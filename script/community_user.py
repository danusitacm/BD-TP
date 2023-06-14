from faker import Faker
import random
n=500000
fake = Faker()
def insert_into_community_user(db_manager):
    values=[]
    query_last_community_id="select community_id from community ORDER BY community_id DESC LIMIT 1"
    last_id_community=db_manager.get_last_id_from_table(query_last_community_id)
    query_last_user_id="select user_id from user_1 ORDER BY user_id DESC LIMIT 1"
    last_id_user=db_manager.get_last_id_from_table(query_last_user_id)
    query="insert into comunnity_user (community_id,user_community_id) VALUES (%s,%s) ON CONFLICT DO NOTHING"
    for i in range(n):
        community_id=random.randint(1,last_id_community)
        user_community_id=random.randint(1,last_id_user)
        values.append((community_id,user_community_id))
    db_manager.executemany_query(query, values)