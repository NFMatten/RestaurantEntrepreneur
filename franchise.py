from sys import float_repr_style
from order import Order
from order_factory import OrderFactory
from logger import Logger

class Franchise:
    def __init__(self, location):
        """
        location_number: int
        """
        self.location_number = location

    # TODO: call the logger.log_transaction() method to log the order to the log.txt file
    def place_order():
        """
        place_order method: void
        """
        print("What would you like to order?")
        user_input = int(input("Type '1' for pizza, '2' for pasta, '3' for salad. "))
        while True:
            if user_input == 1:
                OrderFactory.create_order("Pizza")
                Logger.log_transaction("Pizza")
                return False
            elif user_input == 2:
                OrderFactory.create_order("Pasta")
                return float_repr_style
            elif user_input == 3:
                OrderFactory.create_order("Salad")
                return False
            else:
                print("Invalid selection, please enter 1, 2 or 3. ")
                return True