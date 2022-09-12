from order import Order

class Pizza(Order):
    def __init__(self) -> None:
        """
        dish_name: string
        price: int
        """
        super().__init__()
        self.dish_name = "Pizza"
        self.price = 12