class Logger:
    def __init__(self) -> None:
        """
        instance variables:
            transaction_count: int
            daily_revenue: int
        """
        self.transaction_count = 0
        self.daily_revenue = 0

    def log_transaction(self, Order, store_location):
        """
        Purpose:
            - Increase the Logger's transaction_count by one
            - Add the price of the Order object to the Logger's daily income
            - Open the log.txt file
            - Write a well-formatted message to the log.txt file containing:
                - Current transaction count
                - The name of the dish ordered
                - The store it was ordered from
                - The price of the item
                - The combined daily income
            - Close the log.txt file
        """

        self.transaction_count += 1
        self.daily_revenue += Order.price

        text_file = open("log.txt", "a")
        text_file.write(f"Transaction {self.transaction_count}: {Order.dish_name} at location {store_location} for ${Order.price} Daily Revenue: ${self.daily_revenue}\n")
        text_file.close()

log_order = Logger()
