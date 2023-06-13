from faker import Faker
import random
n=10
fake = Faker()
def insert_into_products(db_manager):
    values=[]
    start_range=1
    end_range=10
    query="INSERT INTO product (product_name,product_price,product_description,game_id,rarity_id) VALUES (%s,%s,%s,%s,%s)"
    for _ in range(n):
        product_name=fake.name()
        product_price=random.uniform(start_range, end_range)
        product_description=fake.text(max_nb_chars=300)
        game_id=random.randint(start_range, end_range)
        rarity_id=random.randint(start_range, 5)
        values.append((product_name,product_price,product_description,game_id,rarity_id))   
    db_manager.executemany_query(query, values)
def insert_into_items(db_manager):
    estados = ['Activo', 'Inactivo', 'Pendiente', 'Finalizado']
    indice_aleatorio = random.randint(0, len(estados) - 1)
    values=[]
    start_range=1
    end_range=10
    query="INSERT INTO items (drop_date,user_id,product_acquired_id,item_status) VALUES (%s,%s,%s,%s)"
    for i in range(n):
        drop_date= fake.date_this_year()
        user_id= random.randint(start_range, end_range)
        product_acquired_id= random.randint(start_range, end_range)
        item_status= estados[indice_aleatorio]
        values.append((drop_date,user_id,product_acquired_id,item_status))
    db_manager.executemany_query(query, values)