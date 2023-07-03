from librerias import *
def insert_into_balance(db_manager):
    n=185000
    values=[]
    start_date=date(2023, 1, 1)
    query_last_user_id="select user_id from user_1 ORDER BY user_id DESC LIMIT 1"
    last_id_user=db_manager.get_last_id_from_table(query_last_user_id)
    query="INSERT INTO balance (amount, description, transaction_date, payment_type, user_balance_id) VALUES (%s,%s,%s,%s,%s)"
    for _ in range(1000):
        for _ in range(185):
            amount=random.randint(700000, 1000000) 
            transaction_date=start_date + timedelta(days=random.randint(0,1))
            description=fake.text(max_nb_chars=300)
            payment_type=random.choice['Tarjetas de crédito o debito','PayPal','Bitcoin','Tarjetas prepagadas']
            user_balance_id=random.randint(1,last_id_user)
            values.append((amount, description, transaction_date, payment_type, user_balance_id))
        start_date = transaction_date + timedelta(days=random.randint(0,5))
    db_manager.executemany_query(query, values)