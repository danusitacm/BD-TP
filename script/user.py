from faker import Faker
n=200000
fake = Faker()
def insert_into_user(db_manager):
    values=[]
    query="INSERT INTO user_1 (banned,start_date,username,password,email) VALUES (%s,%s,%s,%s,%s)"
    for _ in range(n):
        banned=False
        username=fake.user_name()
        date=fake.date()
        password=fake.password()
        email=fake.email()
        values.append((banned,date,username,password,email))   
    db_manager.executemany_query(query, values)
def insert_into_developer(db_manager):
    values=[]
    query="INSERT INTO developer (name,password,email,start_date) VALUES (%s,%s,%s,%s)"
    for _ in range(n):
        name=fake.company()
        password=fake.password()
        email=fake.email()
        date=fake.date()
        values.append((name,password,email,date))   
    db_manager.executemany_query(query, values)