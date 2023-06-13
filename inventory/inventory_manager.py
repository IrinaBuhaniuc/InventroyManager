

class InventoryManager:
    def __init__(self, *products_class):
        self.__products = [P for P in products_class]
        
        
    def check_if_item_exist(self, product_name):
        count= 0
        for item in self.__products[:]:
            if item.name == product_name:   
                return True
        return False
        
    def add_product(self,new_product):
        self.__products.append(new_product)
        return True
        
    def remove_product(self, product_name: str):
        for item in self.__products[:]:
            if item.name == product_name:   
                self.__products.remove(item)
                
    def update_quantities(self, product_name, val):
        for item in self.__products[:]:
            if item.name == product_name:   
                item.update_quantity(val)

            
                
                
    def get_information(self,product_name):
        for item in self.__products[:]:
            if item.name == product_name:   
                return item.get_product_info()
        else:
            return "Product not found"
        
    def get_total_inventory_value(self):
        total_value = 0
        for item in self.__products:
            total_value += item.price * item.quantity
        return float(format(total_value, ".2f"))
    
    def check_if_empty(self):
        if len(self.__products) == 0:
            return True
        return False
            
    
    @property
    def products(self):
        return self.__products
    
    