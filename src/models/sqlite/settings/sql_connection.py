import sqlite3
from sqlite3 import Connection as SqliteConnection


class SqliteConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "storage.db"
        self.__connection = None

    def connect(self) -> SqliteConnection:
        sqlite_conn = sqlite3.connect(self.__connection_string, check_same_thread=False)
        self.__connection = sqlite_conn
        return sqlite_conn
    
    def get_connection(self) -> SqliteConnection:
        return self.__connection
