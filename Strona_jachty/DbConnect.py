import mysql.connector
import json

class ConnectionConfig:
    def __init__(self):
        self.host='localhost'
        self.database='jachty'
        self.user='root'
        self.password='admin007'
        self.connection=mysql.connector.connect(host=self.host,
                                                database=self.database,
                                                user=self.user,
                                                password=self.password)

    def DownloadData(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            return json.dumps(records)
        except mysql.connector.Error as e:
            return str(e)

    def InsertData(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            return 'Ok'
        except mysql.connector.Error as e:
            return str(e)
