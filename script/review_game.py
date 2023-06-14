from faker import Faker
import random
fake = Faker()
def insert_into_game_review(db_manager):
    n = 10000
    values=[]
    query_purchase = "SELECT user_id, game_id FROM user_buy_game ORDER BY RANDOM() LIMIT 1"
    query = "INSERT INTO game_review (description, publish_date, score, title, game_id, user_id) VALUES (%s, %s, %s, %s, %s, %s)"
    for i in range(n):
        description = generate_random_description()
        publish_date = fake.date_this_year()
        score = random.randint(1, 10)
        title = generate_random_title()
        # Obtener una compra aleatoria de la tabla purchase para un usuario que ha comprado un juego
        purchase_data = db_manager.get_data(query_purchase)
        if purchase_data:
            user_id=purchase_data[0][0]
            game_id= purchase_data[0][1]
            values.append((description, publish_date, score, title, game_id, user_id))
    db_manager.executemany_query(query, values)  # Ejecutar la consulta con los valores generados


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