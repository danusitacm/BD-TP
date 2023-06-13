from faker import Faker
import random
from datetime import datetime, timedelta,date
n=100000
fake = Faker()
name_event=('Festival de la Construccion de Bases',
            'Next Fest de febrero','Festival del Misterio',
            'Rebajas de Otono', 'Rebajas de Invierno', 
            'Festival del sigilo', 
            'Rebajas de Primavera','Festival de los Puzles', 
            'Festival de los Deportes', 'Rebajas de Verano', 
            'Festival del sigilo','Festival de los Deportes','Racing Fest',
            'Empanada don vito')

def insert_into_event(db_manager):
    start_date=date(2023, 1, 1)
    values=[]
    query="insert into event (name,description,start_date,end_date) values (%s,%s,%s,%s)"
    for _ in range(n):
        name=random.choice(name_event)
        description=fake.text(max_nb_chars=300)
        random_start_date= start_date + timedelta(days=random.randint(1, 10))
        random_end_date= random_start_date + timedelta(days=random.randint(1, 10))
        start_date = random_end_date
        values.append((name,description,random_start_date,random_end_date))  
    db_manager.executemany_query(query, values)