from flask import Flask
from src.models.redis.settings.redis_connection import RedisConnectionHandler
from src.models.sqlite.settings.sql_connection import SqliteConnectionHandler
from src.main.routes.products_routes import products_routes_bp

redis_conn = RedisConnectionHandler()
sqlite_conn = SqliteConnectionHandler()

redis_conn.connect()
sqlite_conn.connect()

app = Flask(__name__)

app.register_blueprint(products_routes_bp)
