class Computer:
    
    def __init__(self):
        self.__maxprice = 900
        
    def sell(self):
        print(f'Selling price: {self.__maxprice}')
        
    def setMaxPrice(self, price):
        self.__maxprice = price
    
computer1 = Computer()
computer1.sell()

# change to price
computer1.__maxprice = 1000
computer1.sell()

# using setter function

computer1.setMaxPrice(1100)
computer1.sell()