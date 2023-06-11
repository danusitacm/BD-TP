from faker import Faker
import random
""" Discleimer :Esta funcion se puede usar solo una vez ya que no quiero usar while para ver si hay 
valores repetidos, se recomienda eliminar los valores de la tabla y volver a arrancar esta
funcion """ 
def insert_into_game_event(db_manager):
    values=[]
    # Obtenemos el producto cartesiano de la tablas game event
    query="select event_id, game_id from event,game"
    cartesian_product=db_manager.get_cartesian_product(query)    
    #Cargo en mi values los dos id y le añado el descuento
    for i in cartesian_product:
        values.append(i + (round(random.uniform(0.03, 0.8), 1),))
    #Desordenamos los valores        
    random.shuffle(values)
    # Obtener la mitad del tamaño de la lista
    half_size = int(len(values) / 2)
    # Eliminar la mitad de los elementos de forma aleatoria
    for _ in range(half_size):
        values.pop(random.randint(0, len(values) - 1))
    print(values)
    query="insert into game_event (event_id,game_id,discount) values (%s,%s,%s)"
    db_manager.execute_query(query, values)
