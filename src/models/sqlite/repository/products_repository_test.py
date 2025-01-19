import pytest
from src.models.sqlite.settings.sql_connection import SqliteConnectionHandler
from src.models.sqlite.repository.products_repository import ProductsRepository

connection_handler = SqliteConnectionHandler()
connection = connection_handler.connect()

@pytest.mark.skip(reason="Integration test")
def test_insert_product():
    products_repository = ProductsRepository(connection)
    products_repository.insert_product("Product 1", 19.85, 2)
    
@pytest.mark.skip(reason="Integration test")
def test_get_product_by_name():
    products_repository = ProductsRepository(connection)
    product = products_repository.get_product_by_name("Product 1")
    print(product)
