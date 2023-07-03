from librerias import *
n=400000
fake = Faker()
def insert_into_products(db_manager):
    values=[]
    start_range=1
    end_range=10
    query="INSERT INTO product (product_name,producto_price,product_description,game_id,rarity_id) VALUES (%s,%s,%s,%s,%s)"
    query_last_game_id="select game_id from game ORDER BY game_id DESC LIMIT 1"
    last_id_game=db_manager.get_last_id_from_table(query_last_game_id)
    for _ in range(n):
        product_name=fake.name()
        product_price=random.uniform(start_range, end_range)
        product_description=fake.text(max_nb_chars=300)
        game_id=random.randint(1,last_id_game)
        rarity_id=random.randint(start_range, 5)
        values.append((product_name,product_price,product_description,game_id,rarity_id))   
    db_manager.executemany_query(query, values)
def insert_into_items(db_manager):
    estados = ['Activo', 'Inactivo', 'Pendiente', 'Finalizado']
    values=[]
    query_last_user_id="select user_id from user_1 ORDER BY user_id DESC LIMIT 1"
    last_id_user=db_manager.get_last_id_from_table(query_last_user_id)
    query_last_product_id="select product_id from product ORDER BY product_id DESC LIMIT 1"
    last_id_product=db_manager.get_last_id_from_table(query_last_product_id)
    query="INSERT INTO item (drop_date,user_id,product_acquired_id,item_status) VALUES (%s,%s,%s,%s)"
    for i in range(n):
        drop_date= fake.date_this_year()
        user_id=random.randint(1, last_id_user)
        product_acquired_id= random.randint(1, last_id_product)
        item_status=random.choice(estados)
        values.append((drop_date,user_id,product_acquired_id,item_status))
    db_manager.executemany_query(query, values)