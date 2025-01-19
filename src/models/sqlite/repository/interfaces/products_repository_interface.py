from abc import ABC, abstractmethod 

class ProductsRepositoryInterface(ABC):
    @abstractmethod
    def get_product_by_name(self, product_name: str) -> tuple:
        pass

    @abstractmethod
    def insert_product(self, product_name: str, price: float, quantity: int) -> None:
        pass
