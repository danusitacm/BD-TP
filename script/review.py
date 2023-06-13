from faker import Faker
import random
n=300000
fake = Faker()
def insert_into_review_game(db_manager):
    values=[]
    query_last_user_id="select user_id from user_1 ORDER BY user_id DESC LIMIT 1"
    last_id_user=db_manager.get_last_id_from_table(query_last_user_id)
    query_last_game_id="select game_id from game ORDER BY game_id DESC LIMIT 1"
    last_id_game=db_manager.get_last_id_from_table(query_last_game_id)
    query="INSERT INTO game_review (description,publish_date,score,title,game_id,user_id) VALUES (%s,%s,%s,%s,%s,%s)"
    for _ in range(n):
        description=fake.text(max_nb_chars=300)
        publish_date=fake.date_this_year()
        score=round(random.uniform(1,5),1)
        title=fake.word()
        user_id=random.randint(1,last_id_user)
        game_id=random.randint(1,last_id_game)
        #user_has_game = db_manager.check_user_has_game(user_id, game_id)
        """ if not user_has_game:
            print(f"El usuario {user_id} no tiene el juego con ID {game_id}. No se insertará la reseña.")
            continue
        """
        values.append((description,publish_date,score,title,game_id,user_id))   
    db_manager.executemany_query(query, values)