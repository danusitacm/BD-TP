from faker import Faker
import random
n=200000
fake = Faker()
def insert_into_gift(db_manager):
    values=[]
    query_last_user_id="select user_id from user_1 ORDER BY user_id DESC LIMIT 1"
    last_id_user=db_manager.get_last_id_from_table(query_last_user_id)
    query_last_game_id="select game_id from game ORDER BY game_id DESC LIMIT 1"
    last_id_game=db_manager.get_last_id_from_table(query_last_game_id)
    query_last_community_id="select community_id from community ORDER BY community_id DESC LIMIT 1"
    last_id_community=db_manager.get_last_id_from_table(query_last_community_id)
    query="INSERT INTO gift (shipping_date,user_id,game_gift_id,community_gift_id) VALUES (%s,%s,%s,%s)"
    for _ in range(n):
        shipping_date=fake.date_this_year()
        user_id=random.randint(1,last_id_user)
        game_gift_id=random.randint(1,last_id_game)
        community_gift_id=random.randint(1,last_id_community)
       #user_has_game = db_manager.check_user_has_game(user_id,game_id)
        """ if not user_has_game:
            print(f"El usuario {user_id} no tiene el juego con ID {game_id}. No se insertará la reseña.")
            continue
        """
        values.append((shipping_date,user_id,game_gift_id,community_gift_id))   
    db_manager.execute_query(query, values)