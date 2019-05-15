class Company:
    def __init__(self, name):
        self.name = name
        self.price_history = []
    
    def add_price(self, price):
        self.price_history.append(price)

    def calculate_standard_deviation(self):
        print('fs')