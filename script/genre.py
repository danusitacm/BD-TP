from faker import Faker
import random
n=10
fake = Faker()
def insert_into_rarity(db_manager):
    query="INSERT INTO genre (description_genre,genre) VALUES (%s,%s)"
    values=[]
    values.append('Lucha' ,1)
    values.append('Beat Em Up',2)
    values.append('ultra-raro',3)
    values.append('Hack and Slash', 4)
    values.append('Arcade', 5)
    values.append('Plataformas', 6)
    values.append('Disparos', 7)
    values.append('Carreras', 8)
    values.append('Run and Gun', 9)
    values.append('Estrategia', 10)
    values.append('Simulación', 11)
    values.append('Deporte', 12)
    values.append('Aventura', 13)
    values.append('Rol', 14)
    db_manager.execute_query(query, values)
    
def insert_into_genre_game(db_manager):
    start_range=1
    end_range=10
    query="INSERT INTO genre_game (game_id,genre_id) VALUES (%s,%s)"
    game_id=random.randint(start_range, end_range)
    genre_id=random.randint(start_range, end_range)