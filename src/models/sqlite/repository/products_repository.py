from sqlite3 import Connection as SqliteConnection
from src.models.sqlite.repository.interfaces.products_repository_interface import ProductsRepositoryInterface

class ProductsRepository(ProductsRepositoryInterface):
    def __init__(self, sql_conn: SqliteConnection) -> None:
        self.__sql_conn = sql_conn

    def get_product_by_name(self, product_name: str) -> tuple:
        cursor = self.__sql_conn.cursor()
        cursor.execute("SELECT * FROM products WHERE name = ?", (product_name,))
        return cursor.fetchone()
    
    def insert_product(self, product_name: str, price: float, quantity: int) -> None:
        cursor = self.__sql_conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", 
            (product_name, price, quantity)
        )
        self.__sql_conn.commit()

