from faker import Faker
import random
n=10
fake = Faker()
def insert_into_community_user(db_manager):
    values=[]
    for _ in range(n):
        values=[]
        # Obtenemos el producto cartesiano de la tablas game event
        query="select user_id, community_id from user_1,community"
        cartesian_product=db_manager.get_cartesian_product(query)    
        #Cargo en mi values los dos id
        for i in cartesian_product:
            values.append(i)
        # Obtener la mitad del tamaño de la lista
        half_size = int(len(values) / 2)
        # Eliminar la mitad de los elementos de forma aleatoria
        for _ in range(half_size):
            values.pop(random.randint(0, len(values) - 1))
        print(values)
    query="INSERT INTO comunnity_user (community_id,user_community_id) VALUES (%s,%s)"
    db_manager.execute_query(query, values)