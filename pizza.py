from order import Order

class Pizza(Order):
    def __init__(self) -> None:
        """
        super().init parameter: string
        price: int
        """
        super().__init__("Pizza")
        self.price = 12