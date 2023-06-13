from tkinter import *
from tkinter import messagebox
from inventory.product import Product
from inventory.inventory_manager import InventoryManager
import sys

inventory_manager = InventoryManager()

def exit():
    sys.exit(1)

def add_product():
    id = id_input.get()
    name = name_input.get()
    price= price_input.get()
    quantity = quantity_input.get()

    if len(id) == 0 or len(name) == 0 or len(price) == 0 or len(quantity) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:                    
        inventory_manager.add_product(Product(id, name, price, quantity))
        id_input.delete(0, END)
        name_input.delete(0, END)
        price_input.delete(0, END)
        quantity_input.delete(0, END)



def add_product_window():

    add_product_window = Toplevel()
    add_product_window.title("Add new product")
    add_product_window.minsize(400, 400)
    add_product_window.config(padx=50, pady=50)

    menu_label = Label(add_product_window, text = "Product details:", font = ("Arial", 20, "bold"), pady= 10)
    menu_label.grid(column = 1, row= 0)

    
    id_label = Label(add_product_window,text = "ID:", pady=10)
    id_label.grid(column=0, row = 1)
    
    global id_input
    id_input = Entry(add_product_window, width= 20)
    id_input.focus()
    id_input.grid(column=1, row=1)

    name_label = Label(add_product_window,text = "Name:", pady= 10)
    name_label.grid(column=0, row = 2)
    
    global name_input
    name_input = Entry(add_product_window, width= 20)
    name_input.grid(column=1, row=2)
    
    price_label = Label(add_product_window,text = "Price:", pady= 10)
    price_label.grid(column=0, row = 3)
    
    global price_input
    price_input = Entry(add_product_window, width= 20)
    price_input.insert(0, string="EURO")
    price_input.grid(column=1, row=3)    

    quantity_label = Label(add_product_window,text = "Quantity:", pady= 10)
    quantity_label.grid(column=0, row = 4)
    
    global quantity_input
    quantity_input = Entry(add_product_window, width= 20)
    quantity_input.grid(column=1, row=4)
    
    save_button = Button(add_product_window, text = "Save", pady= 5, command = add_product)
    save_button.grid(column=1, row= 5)
    
    back_button = Button(add_product_window, text = "Back", pady= 5, command = add_product_window.destroy)
    back_button.grid(column=2, row= 5)
    
    
def remove_product():
    name = to_remove_name_input.get()
    if len(name) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        
    else:
        if inventory_manager.check_if_item_exist(name):
            inventory_manager.remove_product(name)
            to_remove_name_input.delete(0,END)
        else:
            messagebox.showinfo(title="Oops", message="Product not found!")
            to_remove_name_input.delete(0,END)

        
        
def remove_product_window():

    remove_product_window = Toplevel()
    remove_product_window.title("Remove a product")
    remove_product_window.minsize(400, 400)
    remove_product_window.config(padx=50, pady=50)

    remove_label = Label(remove_product_window, text = "Product to be removed:", font = ("Arial", 20, "bold"), pady= 10)
    remove_label.grid(column = 1, row= 0)
    
    name_label = Label(remove_product_window, text= "Name:", pady=10)
    name_label.grid(column=0, row= 1) 
    
    global to_remove_name_input
    to_remove_name_input = Entry(remove_product_window, width = 20)
    to_remove_name_input.grid(column = 1, row= 1)
    
    remove_button = Button(remove_product_window, text= "Remove", command= remove_product)
    remove_button.grid(column=1, row=2)
    
    back_button = Button(remove_product_window, text= "Back", command= remove_product_window.destroy)
    back_button.grid(column=2, row=2)
    
def to_be_printed():
    element = ''
    for item in inventory_manager.products:
        element = element + item.get_product_info()+'\n' 
    if len(element) == 0:
        return "Database is empty!"
    return element

def report_window():
    report_window = Toplevel()
    report_window.title("All product in system:")
    report_window.minsize(400, 400)
    report_window.config(padx=50, pady=50)

    report = Label(report_window, text=to_be_printed())
    report.grid(column=0, row=1)
    
    back_button = Button(report_window, text= "Back", command= report_window.destroy)
    back_button.grid(column=1, row=2)
    
def change_product_quantity():
    name = change_quantity_name_input.get()
    quantity = quantity_input.get()
    if len(name) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        
    else:
        if inventory_manager.check_if_item_exist(name):
            inventory_manager.update_quantities(name, quantity)
            change_quantity_name_input.delete(0,END)
            quantity_input.delete(0,END)
        else:
            messagebox.showinfo(title="Oops", message="Product not found!")
            change_quantity_name_input.delete(0,END)
            quantity_input.delete(0,END)
            
        
def change_quantity_window():
    change_quantity_window = Toplevel()
    change_quantity_window.title("Change product quantity")
    change_quantity_window.minsize(600, 600)
    change_quantity_window.config(padx=50, pady=50)
    
    title_label = Label(change_quantity_window, text = "For which product do you want to change the quantity?")
    title_label.grid(column = 1, row = 0)
    
    name_label = Label(change_quantity_window, text= "Name:", pady=10)
    name_label.grid(column=0, row= 1) 
    
    global change_quantity_name_input
    change_quantity_name_input = Entry(change_quantity_window, width = 20)
    change_quantity_name_input.grid(column = 1, row= 1)
    
    quantity_label =Label(change_quantity_window, text= "New-Quantity:", pady=10)
    quantity_label.grid(column=0, row= 2)
    
    global quantity_input
    quantity_input = Entry(change_quantity_window, width = 20)
    quantity_input.grid(column=1, row =2)
    
    remove_button = Button(change_quantity_window, text= "Add changes", command= change_product_quantity)
    remove_button.grid(column=1, row=3)
    
    back_button = Button(change_quantity_window, text= "Back", command= change_quantity_window.destroy)
    back_button.grid(column=2, row=3)
    
def get_prod_info():
    name = entered_product_name.get()
    if len(name) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        
    else:
        if inventory_manager.check_if_item_exist(name):
            inventory_manager.get_information(name)
            entered_product_name.delete(0,END)
        else:
            messagebox.showinfo(title="Oops", message="Product not found!")
            entered_product_name.delete(0,END)
    
           
def product_information_window():
    product_information_window = Toplevel()
    product_information_window.title("Product information")
    product_information_window.minsize(600, 600)
    product_information_window.config(padx=50, pady=50)
    
    product_name = Label(product_information_window, text = "Enter the name of the product", font = ("Arial", 20, "bold"))
    product_name.grid(column = 1, row = 0)
    
    product_name = Label(product_information_window, text = "Name", font = ("Arial", 20, "bold"))
    product_name.grid(column = 0, row = 1)
    
    global entered_product_name
    
    entered_product_name = Entry(product_information_window, width = 20)
    entered_product_name.grid(column = 1, row = 1)
    
    search_button = Button(product_information_window, text = "Search", pady= 5, command = get_prod_info)
    search_button.grid(column=1, row= 2)
    
    back_button = Button(product_information_window, text= "Back", command= product_information_window.destroy)
    back_button.grid(column = 2, row = 2)

 

window = Tk()
window.title("Inventory Manager System")
window.minsize(500, 400)
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


menu_label = Label(text = "Menu", font = ("Arial", 25, "bold"))
menu_label.grid(column = 1, row= 1)


add_product_button = Button(text="1. Add a product",justify= "left", width=25, command=add_product_window)
add_product_button.grid(column=1, row=2)


remove_product_button = Button(text="2. Remove a product",justify= "left", width=25, command=remove_product_window)
remove_product_button.grid(column=1, row=3)

change_product_details_button = Button(text="3. Change product quantity", width=25, command=change_quantity_window)
change_product_details_button.grid(column=1, row=4)

get_product_information_button = Button(text="4. Get product information", width=25, command=product_information_window)
get_product_information_button.grid(column=1, row=5)

report_button = Button(text="5. Report", width=25, command=report_window)
report_button.grid(column=1, row=6)

quit_button = Button(text="Exit", width=5, command=exit)
quit_button.grid(column=1, row=8)




window.mainloop()
