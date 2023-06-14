from database_manager import DatabaseManager
from user import insert_into_user,insert_into_developer
from game import insert_into_game,insert_into_user_buy_game
from event import insert_into_event
from game_event import insert_into_game_event
from review_game import insert_into_game_review
from community import insert_into_community
from community_user import insert_into_community_user
from gift import insert_into_gift
from items import insert_into_items, insert_into_products
from rarity import insert_into_rarity
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
    db_manager.disconnect()
    