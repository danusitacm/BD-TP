from imports import *
if __name__ == "__main__":
    db_manager = DatabaseManager(user="postgres", password="12345", host="127.0.0.1", port="5432", database="bd")
    db_manager.connect()
    #insert_into_user(db_manager)
    #insert_into_developer(db_manager)
    #insert_into_event(db_manager)
    #insert_into_game(db_manager)
    #insert_into_game_event(db_manager)
    #insert_into_user_buy_game(db_manager)
    #insert_into_game_review(db_manager)
    #insert_into_community(db_manager)
    #insert_into_community_user(db_manager)
    insert_into_gift(db_manager)
    #insert_into_rarity(db_manager)
    #insert_into_products(db_manager)
    #insert_into_items(db_manager)
    #insert_into_balance(db_manager)
    #insert_into_item_transaction(db_manager)
    db_manager.disconnect()
    