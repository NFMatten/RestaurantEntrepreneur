from order import Order

class Salad(Order):
    def __init__(self):
        """
        super().__init__ parameter: 
            dish_name: string
            price: int
        """
        super().__init__("Salad", 6)