def insert_into_rarity(db_manager):
    query="INSERT INTO rarity (name,scale) VALUES (%s,%s)"
    values=[]
    values.append('normal' ,1)
    values.append('raro',2)
    values.append('ultra-raro',3)
    values.append('Epico', 4)
    values.append('legendario', 5)
    db_manager.executemany_query(query, values)