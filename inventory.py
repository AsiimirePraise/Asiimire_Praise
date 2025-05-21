#helper function to display the input prompt
def display():
    return input("\nEnter the item name: ")

def inventory():
    # Items to store the items entered
    items = []
    print("---------My Sample Inventory----------")
    print("Instructions:")
    print("To add items please enter the item name and quantity")
    print("To see all items type 'show'")
    print("To delete all items type 'delete'")
    print("Type 'exit' to terminate the program")
    
    while True:
        itemToStore = display()
        #checks the input
        if itemToStore == "exit":
            break
        
        elif itemToStore == "show":
            if len(items) > 0:
                print("\nItems in inventory:")
                for item in items:
                    print(item)
            else:
                print("No items are present")
                
        elif itemToStore=="delete":
            if(len(items)>0):
                choice=input("are you sure you want to delete all the items(yes/no)?")
                if choice=="yes":
                    items.clear()
                    print("all items have been deleted")
            else:
                print("No items are present to delete")    
        else:
            if itemToStore in items:
                print("item already exists: ")
            
            choice = input("Are you sure you want to add this item (yes/no)? ")
            if choice == "yes":
                items.append(itemToStore)
                print("Item added")
        
inventory()