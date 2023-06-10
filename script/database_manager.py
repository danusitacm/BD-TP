import psycopg2

class DatabaseManager:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.connection = None
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )
            print("Connection to PostgreSQL was successful")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL:", error)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("PostgreSQL connection is closed")

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.executemany(query, params)
            else:
                cursor.executemany(query)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Record(s) affected")
            cursor.close()
        except (Exception, psycopg2.Error) as error:
            print("Failed to execute query:", error)
            
    def check_user_has_game(self, user_id, game_id):
        query = "SELECT COUNT(*) FROM user_buy_game WHERE user_id = %s AND game_id = %s"
        self.cursor.execute(query, (user_id, game_id))
        count = self.cursor.fetchone()[0]
        return count > 0
