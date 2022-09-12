from order import Order

class Pasta(Order):
    def __init__(self) -> None:
        """
        super().init parameter: string
        price: int
        """
        super().__init__("Pasta")
        self.price = 9