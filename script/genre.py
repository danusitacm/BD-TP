from librerias import *

def insert_into_genre(db_manager):
    query_insert_genre="INSERT INTO genre (description_genre,genre) VALUES (%s,%s)"
    values=[]
    values.append(('Lucha',1))
    values.append(('Beat Em Up',2))
    values.append(('ultra-raro',3))
    values.append(('Hack and Slash', 4))
    values.append(('Arcade', 5))
    values.append(('Plataformas', 6))
    values.append(('Disparos', 7))
    values.append(('Carreras', 8))
    values.append(('Run and Gun', 9))
    values.append(('Estrategia', 10))
    values.append(('Simulación', 11))
    values.append(('Deporte', 12))
    values.append(('Aventura', 13))
    values.append(('Rol', 14))
    db_manager.executemany_query(query_insert_genre, values)
    
def insert_into_genre_game(db_manager):
    num_records=185000
    query_last_game_id="select game_id from game ORDER BY game_id DESC LIMIT 1"
    last_game_id=db_manager.get_last_id_from_table(query_last_game_id)
    query_last_genre_id="select genre_id from genre ORDER BY genre_id DESC LIMIT 1"
    last_genre_id=db_manager.get_last_id_from_table(query_last_genre_id)
    values=[]
    query_insert_genre_game="INSERT INTO genre_game (game_id,genre_id) VALUES (%s,%s) ON CONFLICT DO NOTHING"
   
    for _ in range(num_records):
        game_id=random.randint(1, last_game_id)
        genre_id=random.randint(1, last_genre_id)
        values.append((game_id,genre_id))
    
    db_manager.executemany_query(query_insert_genre_game, values)