from librerias import *
def generate_random_description(score):
    if score < 3:
        descripciones_negativas = [
            "Me decepcionó completamente. El coleccionable no cumplió mis expectativas.",
            "No recomendaría este vendedor. El coleccionable llegó dañado y la calidad es deficiente.",
            "Una experiencia de compra terrible. No volvería a adquirir un coleccionable de este vendedor."
        ]
        return random.choice(descripciones_negativas)
    else:
        descripciones_positivas = [
            "¡Increíble adición a mi colección de juegos! Este coleccionable es una verdadera joya. La atención al detalle y la calidad son impresionantes.",
            "No podía resistirme a este coleccionable. Desde el momento en que lo vi, supe que tenía que tenerlo. Ahora ocupa un lugar destacado en mi estantería de juegos.",
            "Esta compra fue un verdadero hallazgo. No solo obtuve un coleccionable raro, sino que también me llegó en perfectas condiciones. ¡Es un tesoro para cualquier fanático de los juegos!"
        ]
        return random.choice(descripciones_positivas)

def generate_random_title(score):
    if score < 3:
        titulos_negativos = [
            "Mala experiencia: artículo de baja calidad",
            "Decepcionado con la compra",
            "No recomiendo este vendedor"
        ]
        return random.choice(titulos_negativos)
    else:
        titulos_positivos = [
            "Experiencia excepcional: ¡Un vendedor confiable de coleccionables de juegos!",
            "¡Muy satisfecho con mi compra!",
            "El mejor vendedor de coleccionables de juegos"
        ]
        return random.choice(titulos_positivos)

def insert_into_item_transaction(db_manager):
    num_records=200000
    values_item_trans=[]
    values_user_review=[]
    start_date=date(2023, 1, 1)
    query_last_user_id="select user_id from user_1 ORDER BY user_id DESC LIMIT 1"
    last_user_id=db_manager.get_last_id_from_table(query_last_user_id)
    query_last_item_id="select item_id from item ORDER BY item_id DESC LIMIT 1"
    last_item_id=db_manager.get_last_id_from_table(query_last_item_id)
    query_insert_item_transacction="INSERT INTO item_transacction (user_seller_id,purchase_date, price, user_buyer_id, item_sell_id) VALUES (%s,%s,%s,%s,%s)"
    query_insert_user_review="INSERT INTO public.user_review(publish_date, title, description, score, user_seller_id, user_reviewer_id) VALUES (%s,%s,%s,%s,%s,%s)"
    
    for _ in range(10):
        for _ in range(10):
            price=random.randint(70000, 1000000) 
            purchase_date=start_date 
            item_sell_id=random.randint(1,last_item_id)
            user_seller_id=random.randint(1,last_user_id)
            user_buyer_id=1+random.randint(1,last_user_id)
            score=random.randint(0,5)
            title=generate_random_title(score)
            description=generate_random_description(score)
            values_item_trans.append((user_seller_id,purchase_date, price, user_buyer_id, item_sell_id))
            values_user_review.append((purchase_date, title, description, score, user_seller_id, user_buyer_id))
        start_date = purchase_date + timedelta(days=random.randint(0,1))
    
    db_manager.executemany_query(query_insert_item_transacction, values_item_trans)
    
    db_manager.executemany_query(query_insert_user_review, values_user_review)

