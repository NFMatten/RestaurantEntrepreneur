from order import Order

class BreadSticks(Order):
    def __init__(self) -> None:
        """
        dish_name: string
        price: int
        """
        super().__init__()
        self.dish_name = "Break Sticks"
        self.price = 6