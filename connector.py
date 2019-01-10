import mysql.connector


class Connector():
    def __init__(self):
        'Connect to the database'
        self.connection = connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Hanze",
            database="hanze"
        )
        self.cursor = connection.cursor()
        print("Connected")


    def get(self, operation):
        self.cursor.execute(operation)
        return self.cursor.fetchall()


    def execute(self, operation):
        self.cursor.execute(operation)
        self.connection.commit()
        # cursor.reset()


    def __del__(self):
        """ Closes the connection to the database """
        try:
            # self.cursor.close() # Werkt niet als global
            self.connection.close()
        except:
            pass
        print("Disconnected")


connector = Connector()

if __name__ == "__main__":
    def main():
        # connector.create()
        pass
    main()