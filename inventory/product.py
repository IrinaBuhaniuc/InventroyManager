from datetime import date

class Product:
    def __init__(self, id: int, name: str, price: float, quantity: int, entry_date=date.today()):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__entry_date = entry_date 
        
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @property
    def entry_date(self):
        return self.__entry_date
    
    # @price.setter
    # def price(self, val):
    #     self.__price = val
    
    # @price.setter
    # def name(self, val):
    #     self.__price = val
        
        
    def update_quantity(self, val):
        self.__quantity = val
    
    def update_name(self, val):
        self.__name = val
    
    def update_price(self,val):
        self.__price = val
        
    def get_product_info(self):
        return f'''ID.:<{self.__id}>
                   Name: {self.__name}
                   Costs: {self.price} EURO
                   Available quantity: {self.quantity}
                   Entered date: {self.entry_date}'''