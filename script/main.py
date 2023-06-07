from database_manager import DatabaseManager
from user import insert_into_user,insert_into_developer
from game import insert_into_game
from event import insert_into_event

if __name__ == "__main__":
    db_manager = DatabaseManager(user="postgres", password="12345", host="127.0.0.1", port="5432", database="bd")
    insert_into_event(True)
    db_manager.connect()
    db_manager.disconnect()
    