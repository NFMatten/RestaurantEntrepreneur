class Logger:
    def __init__(self) -> None:
        """
        transaction_count: int
        daily_revenue: int
        """
        self.transaction_count = 0
        self.daily_revenue = None

    def log_transaction(self):
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
        self.daily_revenue += 0 # 0 will be current order cost

        text_file = open("log.txt", "a")
        text_file.write("Transaction {transaction_count}: {dish_name} {store_name} ${price} ${daily_revenue}\n")
        text_file.close()
