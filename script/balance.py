from librerias import *
def insert_into_balance(db_manager):
    values=[]
    metodos_de_pago = ['Tarjetas de crédito o débito', 'PayPal', 'Bitcoin', 'Tarjetas prepagadas']
    query_last_purchase_id="SELECT user_buy_game FROM user_buy_game ORDER BY user_buy_game DESC LIMIT 1"
    last_purchase_id=db_manager.get_last_id_from_table(query_last_purchase_id)
    query_insert_balance = "INSERT INTO balance (amount, description, transaction_date, payment_type, user_balance_id) VALUES (%s,%s,%s,%s,%s)"
    
    for _ in range(1000):
        for _ in range(185):
            description=fake.text(max_nb_chars=300)
            payment_type=random.choice(metodos_de_pago)
            id_purchase=random.randint(1,last_purchase_id)
            query_purchase = f"SELECT user_id, total_price, purchase_date FROM user_buy_game WHERE user_buy_game={id_purchase} LIMIT 1"
            purchase_data = db_manager.get_data(query_purchase)
            if purchase_data:
                user_balance_id=purchase_data[0][0]
                amount= purchase_data[0][1]
                transaction_date=purchase_data[0][2]
            values.append((amount, description, transaction_date, payment_type, user_balance_id))
    
    db_manager.executemany_query(query_insert_balance, values)