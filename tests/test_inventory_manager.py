import unittest
from inventory.product import Product
from inventory.inventory_manager import InventoryManager
from datetime import date

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product(1, "TeddyBear", 10.99, 2)
        
    def test_get_product_info(self):
        
        # Arrange
        #product = Product(1, "TeddyBear", 10.99, 2)
        
        # Act
        expected_result = f'''ID.:<1>
                   Name: TeddyBear
                   Costs: 10.99 EURO
                   Available quantity: 2
                   Entered date: {date.today()}'''
                   
        result = self.product.get_product_info()
        
        #Assert
        self.assertEqual(expected_result, result)
        
class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.inventory_manager = InventoryManager()
        
    def test_add_product(self):
        #Arrange
        new_product = (1, "TeddyBear", 10.99, 2)
        #Act   
        result = self.inventory_manager.add_product(new_product)
        #Assert
        self.assertTrue(result)
    
    def test_remove_product(self):
        
        self.assertEquals(len(self.inventory_manager.products), 0)
        
    
    
    
    # don't work, have to check!
    def test_update_quantity(self):
        #Arrange
        new_product = (1, "TeddyBear", 10.99, 2)   
        self.inventory_manager.add_product(new_product)
        
        #Act
        
        self.inventory_manager.update_quantities("TeddyBear", 4) 
        expected_result = 4
        
        result = self.inventory_manager.products[0].quantity
        
        #Assert
        
        self.assertEquals(result, expected_result)