from faker import Faker
n=10
fake = Faker()
def insert_into_community(db_manager):
    values=[]
    query="INSERT INTO community (name,description) VALUES (%s,%s)"
    for _ in range(n):
        name=fake.word()
        description=fake.text(max_nb_chars=300)
        values.append((name,description))   
    db_manager.execute_query(query, values)