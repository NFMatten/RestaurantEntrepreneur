from order_factory import OrderFactory
from logger import log_order

class Franchise:
    def __init__(self, location):
        """
        parameter:
            location: int
        instance variable:
            self.location = int
        """
        self.location = location

    def place_order(self):
        """
        place_order method: void
        """
        
        invalid_selection = True
        while invalid_selection:

            self.print_welcome(self.location)
            user_input = int(input("Type '1' for pizza, '2' for pasta, '3' for salad.\n"))

            if user_input == 1:
                log_order.log_transaction(OrderFactory.create_order("Pizza"), self.location)
                invalid_selection = False

            elif user_input == 2:
                log_order.log_transaction(OrderFactory.create_order("Pasta"), self.location)
                invalid_selection = False

            elif user_input == 3:
                log_order.log_transaction(OrderFactory.create_order("Salad"), self.location)
                invalid_selection = False

            else:
                print("Invalid selection, please enter 1, 2 or 3. ")
                invalid_selection = True

    def print_welcome(self, location):
        print(f"\nWelcome to Giordano's, location {location}!")
        print("What would you like to order?")