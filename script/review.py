from faker import Faker
import random
n=10
fake = Faker()
def insert_into_review(db_manager):
    values=[]
    start_range=1
    end_range=10
    query="INSERT INTO game_review (description,publish_date,score,game_id,user_id) VALUES (%s,%s,%s,%s,%s)"
    for _ in range(n):
        description=fake.text(max_nb_chars=300)
        publish_date=fake.date_this_year()
        score=random.uniform(start_range,5)
        game_id=random.randint(start_range, end_range)
        user_id=random.randint(start_range, end_range)
        
        user_has_game = db_manager.check_user_has_game(user_id, game_id)
        if not user_has_game:
            print(f"El usuario {user_id} no tiene el juego con ID {game_id}. No se insertará la reseña.")
            continue
        
        values.append((description,publish_date,score,game_id,user_id))   
    db_manager.execute_query(query, values)