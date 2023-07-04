from librerias import *

fake = Faker()
def insert_into_user(db_manager):
    num_records=800000
    values=[]
    query_insert_user="INSERT INTO user_1 (banned,start_date,username,password,email) VALUES (%s,%s,%s,%s,%s)"
    
    for _ in range(num_records):
        banned=False
        username=fake.user_name()
        date=fake.date()
        password=fake.password()
        email=fake.email()
        values.append((banned,date,username,password,email))   
    
    db_manager.executemany_query(query_insert_user, values)

def insert_into_developer(db_manager):
    num_records=185000
    values=[]
    query_insert_developer="INSERT INTO developer (name,password,email,start_date) VALUES (%s,%s,%s,%s)"
   
    for _ in range(num_records):
        name=fake.company()
        password=fake.password()
        email=fake.email()
        date=fake.date()
        values.append((name,password,email,date))   
    
    db_manager.executemany_query(query_insert_developer, values)