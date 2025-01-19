from src.models.redis.repository.interfaces.redis_repository_interface import RedisRepositoryInterface
from src.models.sqlite.repository.interfaces.products_repository_interface import ProductsRepositoryInterface

class ProductFinder:
    def __init__(self, redis_repo: RedisRepositoryInterface, products_repo: ProductsRepositoryInterface) -> None:
        self.__redis_repo = redis_repo
        self.__products_repo = products_repo

    
