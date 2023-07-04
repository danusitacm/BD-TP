from librerias import *
def insert_into_game_review(db_manager):
    n = 100000
    values=[]
    query = "INSERT INTO game_review (description, publish_date, score, title, game_id, user_id) VALUES (%s, %s, %s, %s, %s, %s)"
    query_purchase = "SELECT user_id, game_id FROM user_buy_game ORDER BY RANDOM() LIMIT 1"
    query_last_id_purchase="SELECT user_buy_game FROM user_buy_game ORDER BY user_buy_game DESC LIMIT 1"
    last_id_purchase=db_manager.get_last_id_from_table(query_last_id_purchase)
    for i in range(n):
        score = random.randint(1, 10)
        description = generate_random_description(score)
        title = generate_random_title(score)
        publish_date = fake.date_this_year()
        # Obtener una compra aleatoria de la tabla purchase para un usuario que ha comprado un juego
        id_purchase=random.randint(1,last_id_purchase)
        query_purchase = f"SELECT user_id, game_id FROM user_buy_game WHERE user_buy_game={id_purchase} LIMIT 1"
        purchase_data = db_manager.get_data(query_purchase)
        if purchase_data:
            user_id=purchase_data[0][0]
            game_id= purchase_data[0][1]
            values.append((description, publish_date, score, title, game_id, user_id))
    db_manager.executemany_query(query, values)  # Ejecutar la consulta con los valores generados


def generate_random_description(score):
    if score < 5:
        descriptions_negativas = [
            "No me gustó el juego, no lo recomendaría",
            "No vale la pena el dinero",
            "Tiene muchos errores y problemas"
        ]
        return random.choice(descriptions_negativas)
    else:
        descriptions_positivas = [
            "Gran juego, lo recomiendo totalmente",
            "Una experiencia asombrosa",
            "Es divertido y adictivo"
        ]
        return random.choice(descriptions_positivas)


def generate_random_title(score):
    if score < 5:
        titles_negativos = [
            "No recomendaría este juego",
            "Decepcionante",
            "No vale la pena"
        ]
        return random.choice(titles_negativos)
    else:
        titles_positivos = [
            "Una experiencia inolvidable",
            "Recomendado",
            "Divertido y emocionante"
        ]
        return random.choice(titles_positivos)