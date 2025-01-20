from src.models.redis.repository.interfaces.redis_repository_interface import RedisRepositoryInterface
from src.models.sqlite.repository.interfaces.products_repository_interface import ProductsRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class InsertProduct:
    def __init__(self, redis_repo: RedisRepositoryInterface, products_repo: ProductsRepositoryInterface) -> None:
        self.__redis_repo = redis_repo
        self.__products_repo = products_repo

    def insert_product(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        name = body["name"]
        price = body["price"]
        quantity = body["quantity"]
        self.__insert_product_in_db(name, price, quantity)
        self.__insert_product_in_cache(name, price, quantity)
        return self.__format_response()

    def __insert_product_in_db(self, name: str, price: float, quantity: int) -> None:
        self.__products_repo.insert_product(name, price, quantity)

    def __insert_product_in_cache(self, name: str, price: float, quantity: int) -> None:
        product_data = f"{price},{quantity}"
        self.__redis_repo.insert_key_ex(name, product_data, ex=60)

    def __format_response(self) -> HttpResponse:
        return HttpResponse(status_code=201, body={
            "type": "product",
            "message": "Product inserted"
        })
