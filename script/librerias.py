from faker import Faker
fake = Faker()
import random
from datetime import datetime, timedelta, date
import time
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
from balance import insert_into_balance