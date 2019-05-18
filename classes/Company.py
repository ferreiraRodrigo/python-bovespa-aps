import numpy as np

class Company:
    def __init__(self, name):
        self.name = name
        self.price_open_history = []
        self.price_close_history = []
    
    def add_price(self, price_open, price_close):
        self.price_open_history.append(price_open)
        self.price_close_history.append(price_close)

    # Return the standard deviation as a risk for every company
    def get_standard_deviation(self):
        return np.std(self.price_close_history)

    # Return the arithmetic mean of every company profit(relative value)
    def get_average_profit(self):
        profit_history = []
        for i in range(len(self.price_open_history)):
            profit_history.append((self.price_close_history[i] - self.price_open_history[i]) * 100 / self.price_close_history[i])
        
        return sum(profit_history) / len(profit_history)
    
    def get_profit_history(self):
        profit_history = []
        for i in range(len(self.price_open_history)):
            profit_history.append((self.price_close_history[i] - self.price_open_history[i]) * 100 / self.price_close_history[i])
        
        return profit_history