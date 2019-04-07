import pymysql as MySQLdb
import sys
from singleton import Singleton


class MySQLConnection:
    connection = None
    cursor = None

    def __init__(self):
        try:
            self.config = Singleton
            self.connection = self.initConnection()
            self.cursor = self.initCursor()
        except:
            print(
                "Topology Module : Unexpected error While Initializing Database Connection.\n Terminating Application",
                sys.exc_info())

    def initConnection(self):
        con = MySQLdb.connect(host=self.config.db_host, port=self.config.db_port, user=self.config.db_username,
                              passwd=self.config.db_password, db=self.config.db_schema)
        return con

    def initCursor(self):
        cur = self.connection.cursor()
        return cur

    def getConnection(self):
        return self.connection

    def getCursor(self):
        return self.cursor

    def __del__(self):
        self.cursor.close()
        self.connection.close()
