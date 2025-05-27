import numpy as np
from multipledispatch import dispatch

#store customers as objects in an array
customers = np.empty(0, dtype=object)
#base class
class User:
    def __init__(self, name, contact, email):
        self.name = name
        self.contact = contact
        self.email = email

    def add_to_cart(self, item):
        print(f"Successfully added to cart: {item}")

    def make_order(self):
        print(f"{self.name} is making an order.")

    def view_order(self):
        print(f"{self.name} wants to view an order.")

    def display_order_info(self):
        print("Displaying order history.")

#Admin class
class Admin(User):
    def __init__(self, name, contact, email, adminID):
        super().__init__(name, contact, email)
        self.adminID = adminID

    def view_order(self, customerID):
        print(f"\nAdmin wants to view order for customer ID: {customerID}")
        found = False
        for cust in customers:
            if cust.customerID == customerID:
                cust.display_order_info()
                found = True
                break
        if not found:
            print("The customer ID does not exist.")
#Customer class
class Customer(User):
    def __init__(self, name, contact, email, customerID, orderNo):
        super().__init__(name, contact, email)
        self.customerID = customerID
        self.orderNo = orderNo
        self.cart = []

        global customers
        customers = np.append(customers, self)

    def display_order_info(self):
        print(f"Customer {self.name} has order number {self.orderNo}. Cart: {self.cart}")

    def make_order(self):
        if not self.cart:
            print(f"{self.name}'s cart is empty. Add items before making an order.")
        else:
            print(f"{self.name} has made an order with the following items: {self.cart}")
#overload add to cart
    @dispatch(str)
    def add_to_cart(self, item):
        self.cart.append((item, 1))
        print(f"{self.name} added 1 unit of {item} to the cart.")
#overload add to cart
    @dispatch(str, int)
    def add_to_cart(self, item, quantity):
        self.cart.append((item, quantity))
        print(f"{self.name} added {quantity} units of {item} to the cart.")

#prime customer 
class PrimeCustomer(Customer,User):
    def __init__(self, name, contact, email, customerID, orderNo, primeID):
        super().__init__(name, contact, email, customerID, orderNo)
        self.primeID = primeID

print("---------------------------------------------------------------")
cust = Customer("Asiimire", "1234567890", "asiimire@gmail.com", "C123", "O001")
cust.add_to_cart("Shoes")
cust.add_to_cart("Shirt", 2)
cust.display_order_info()
cust.make_order()

print("---------------------------------------------------------------")
prime = PrimeCustomer("Praise", "0987654321", "praiseAsiimire@gmail.com", "PC101", "O102", 250)
prime.add_to_cart("Laptop", 1)
prime.display_order_info()

print("---------------------------------------------------------------")
admin = Admin("Praise", 9898, "Praise@gmail.com", "AD09")
admin.view_order("C123")  
admin.view_order("XYZ999") 
