from order import Order

class Salad(Order):
    def __init__(self) -> None:
        """
        super().init parameter: string
        price: int
        """
        super().__init__("Salad")
        self.price = 6