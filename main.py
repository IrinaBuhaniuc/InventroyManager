from inventory.product import Product
from inventory.inventory_manager import InventoryManager
import sys

# prod1 = Product(1,"TeddyBear",15.69, 2)
# prod2 = Product(2,"Bike",159.99, 5)
# prod3 = Product(3,"Book",4.99, 3)

# # print(prod1.get_product_info())
# # print(prod2.get_product_info())


inventory_manager = InventoryManager()


print("**Welcome to IMS-Store**")
print("")
while True:
    print('''**Menu:**
        1. Add a product.
        2. Remove a product.
        3. Change product details.
        4. Get product information.
        5. Report.
        6. Quit''')
    option = input(("Please select an option from **Menu**: "))
    
    if option == "1":
        print("\nPlease enter product details: \n")
        id = int(input("ID Number: "))
        name = input("NAME:  ")
        price = float(input("PRICE: "))
        quantity = int(input("QUANTITY: "))
        inventory_manager.add_product(Product(id, name, price, quantity))
    
    elif option == "2":
        if not inventory_manager.check_if_empty():
            remove_item = input("Please enter name of the product you want to remove: ")
            inventory_manager.remove_product(remove_item)
        else: 
            print("Database is empty, please first add some data.")
    elif option == "3":
        if not inventory_manager.check_if_empty():
            product_name = input("For which product do you want to change details?: ")
            print(f"{inventory_manager.get_information(product_name)}")
            print('''Chose from the option bellow, what do you want to change: 
                1. NAME
                2. PRICE
                3. QUANTITY
                ''')
            detail = input(">> ")
            if detail == "1":
                print("NotImplemented")
            elif detail == "2":
                print("NotImplemented")
            elif detail == "3":
                update_quant = int(input("New quantity: "))
                inventory_manager.update_quantities(product_name, update_quant) 
        else: 
            print("Database is empty, please first add some data.")
            
    elif option == "4":
        print("NotImplemented")
    
    elif option == "5":
        print("NotImplemented")
    
    elif option == "6":
        print("Good Bye!")
        sys.exit(1)
    else: 
        print("Please enter a valid option number.")

# for product in inventory_manager.products:
#     print(product.get_product_info())

# print(inventory_manager.get_information("Headphones"))

# print(inventory_manager.get_information("Diamond_ring"))

#print(inventory_manager.get_total_inventory_value())

