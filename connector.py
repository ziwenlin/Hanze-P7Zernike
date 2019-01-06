import mysql.connector


class Connector():
    def __init__(self):
        'Connect to the database'
        self.connection = connection = mysql.connector.connect(
            host="localhost",
            user="hanze",
            passwd="",
            database="hanze"
        )
        self.cursor = connection.cursor()
        print("Connected")


    def get(self, operation):
        self.cursor.execute(operation)
        return self.cursor


    def execute(self, operation):
        self.cursor.execute(operation)
        self.connection.commit()
        # cursor.reset()


    def __del__(self):
        """ Closes the connection to the database """
        # self.cursor.close() # Werkt niet met global
        self.connection.close()
        print("Disconnected")


connector = Connector()