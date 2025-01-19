from src.models.redis.repository.interfaces.redis_repository_interface import RedisRepositoryInterface
from src.models.sqlite.repository.interfaces.products_repository_interface import ProductsRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class ProductFinder:
    def __init__(self, redis_repo: RedisRepositoryInterface, products_repo: ProductsRepositoryInterface) -> None:
        self.__redis_repo = redis_repo
        self.__products_repo = products_repo

    def get_product_by_name(self, http_request: HttpRequest) -> HttpResponse:
        product_name = http_request.params["product_name"]
        product = self.__get_product_from_cache(product_name)
        if not product:
            product = self.__get_product_from_db(product_name)
            self.__insert_product_in_cache(product)
        return self.__format_response(product)
    
    def __get_product_from_cache(self, product_name: str) -> tuple:
        product = self.__redis_repo.get_key(product_name)
        if product:
            product_list = product.split(",")
            return (0, product_name, product_list[0], product_list[1])
        return None
    
    def __get_product_from_db(self, product_name: str) -> tuple:
        product = self.__products_repo.get_product_by_name(product_name)
        if not product:
            raise Exception("Product not found")
        return product
    
    def __insert_product_in_cache(self, product: tuple) -> None:
        product_name = product[1]
        product_data = f"{product[2]},{product[3]}"
        self.__redis_repo.insert_key_ex(product_name, product_data, ex=60)

    def __format_response(self, product: tuple) -> HttpResponse:
        return HttpResponse(status_code=200, body={
            "type": "product",
            "attributes": {
                "name": product[1],
                "price": product[2],
                "description": product[3]
            }
        })
