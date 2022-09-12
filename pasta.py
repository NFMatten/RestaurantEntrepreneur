from order import Order

class Pasta(Order):
    def __init__(self) -> None:
        """
        dish_name: string
        price: int
        """
        super().__init__()
        self.dish_name = "Pasta"
        self.price = 9