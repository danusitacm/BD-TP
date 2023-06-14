import random
import datetime

def insert_into_game_review(db_manager):
    n = 20000
    query_last_game_id = "SELECT game_id FROM game ORDER BY game_id DESC LIMIT 1"
    last_id_game = db_manager.get_last_id_from_table(query_last_game_id)
    query_last_user_id = "SELECT user_id FROM user ORDER BY user_id DESC LIMIT 1"
    last_id_user = db_manager.get_last_id_from_table(query_last_user_id)

    db_manager.connection.begin()  # Iniciar la transacción explícita

    try:
        for i in range(n):
            game_review_id = i + 1  # Incrementar el ID de revisión del juego
            description = generate_random_description()
            publish_date = generate_random_publish_date()
            score = random.randint(1, 10)
            title = generate_random_title()

            # Obtener una compra aleatoria de la tabla purchase para un usuario que ha comprado un juego
            query_purchase = "SELECT user_id, game_id FROM purchase ORDER BY RANDOM() LIMIT 1"
            purchase_data = db_manager.get_data(query_purchase)
            if purchase_data:
                user_id, game_id = purchase_data[0]

                query = "INSERT INTO game_review (game_review_id, description, publish_date, score, title, game_id, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (game_review_id, description, publish_date, score, title, game_id, user_id)

                db_manager.execute_query(query, values)  # Ejecutar la consulta con los valores generados

        db_manager.connection.commit()  # Confirmar los cambios en la transacción
    except:
        db_manager.connection.rollback()  # En caso de error, deshacer los cambios realizados

def generate_random_description():
    # Generar una descripción aleatoria (puedes personalizarlo según tus necesidades)
    descriptions = [
        "Gran juego, lo recomiendo totalmente",
        "La jugabilidad es increíble, pero los gráficos podrían mejorar",
        "No me gustó el juego, no lo recomendaría",
        "¡Una experiencia asombrosa! Sin duda uno de los mejores juegos que he jugado",
        "Es divertido y adictivo, pero tiene algunos errores"
    ]
    return random.choice(descriptions)

def generate_random_publish_date():
    # Generar una fecha de publicación aleatoria dentro de un rango específico (puedes personalizarlo según tus necesidades)
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2022, 12, 31)
    random_date = random.choice([start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days)])
    return random_date

def generate_random_title():
    # Generar un título aleatorio (puedes personalizarlo según tus necesidades)
    titles = [
        "Una experiencia inolvidable",
        "Buen juego, pero tiene sus problemas",
        "No vale la pena el dinero",
        "Altamente recomendado",
        "Divertido pero desafiante"
    ]
    return random.choice(titles)