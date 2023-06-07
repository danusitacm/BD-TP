from faker import Faker
import random
from datetime import datetime, timedelta
n=10
fake = Faker()
name_event=('Festival de la Construcción de Bases',
            'Next Fest de febrero','Festival del Misterio',
            'Rebajas de Otoño', 'Rebajas de Invierno', 
            'Festival del sigilo', 
            'Rebajas de Primavera','Festival de los Puzles', 
            'Festival de los Deportes', 'Rebajas de Verano', 
            'Festival del sigilo','Festival de los Deportes')
def insert_into_event(db_manager):
    values=[]
    query="INSERT INTO event (name,description,start_date,end_date) VALUES (%s,%s,%s,%s)"
    for _ in range(n):
        name=random.choice(name_event)
        description=fake.text(max_nb_chars=300)
        start_date=fake.date_between(start_date=datetime(2023,1,1), end_date='+30d')
        end_date=fake.date_between(start_date=start_date, end_date=datetime(2023,12,31))
        values.append((name,description,start_date,end_date))  
    db_manager.execute_query(query, values)