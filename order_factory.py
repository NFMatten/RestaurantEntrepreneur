from pizza import Pizza
from pasta import Pasta
from salad import Salad

class OrderFactory:

    @staticmethod
    def create_order(dish_name):
        """
        create_order method: static
        Parameter:
            dish_name: string
        """
        if dish_name == "Pizza":
            return Pizza()
        elif dish_name == "Pasta":
            return Pasta()
        elif dish_name == "Salad":
            return Salad()
 