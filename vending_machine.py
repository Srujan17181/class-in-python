# create a vending machine class that manages its inventory and cash,ensuring that items can only be dispensed 
# if the correct payment is made and the item is in stock

class vending_machine():
    def __init__(self):
        self.items={
        "book":40,
        "pens":30,
        "pencil":20,
        "eraser":10,
        }
        self.price={"book":25,
                    "pens":10,
                    "pencil":5,
                    "eraser":3}
        self.cash_box=0

    def get_stock(self,name_items,price_items):
        if name_items in self.items.keys():
            if self.price[name_items]==price_items:
                self.items[name_items]-=1 
                return f"your item is {name_items} and {self.price[name_items]} \n you fetched item successfully "

    def view_stocks(self):
        return f"you have stocks {self.items.items()}"
    
    def start_functioning(self,choice):
        print(f"$ ITEMS and its PRICE {main.price.items()}")
        if choice=="start":
            get_items=input("Enter the item which you want: ")
            put_price=int(input("enter the correct price of choosed items: "))
            print(main.get_stock(get_items,put_price))
        elif choice=="view_stack":
            print(f"stock in store is {main.view_stocks()}")


    

main=vending_machine()
choice=input("If you want to exit enter space or want to view the stack ")




# print("------------welcome to vending store-----------")
# print(f"$ ITEMS and its PRICE {main.price.items()}")

# start=True
# while start:
#     print(f"$ ITEMS and its PRICE {main.price.items()}")
#     choice=input("If you want to exit enter space or want to view the stack ")
    
    
#     if choice=="start":
#         get_items=input("Enter the item which you want: ")
#         put_price=int(input("enter the correct price of choosed items: "))
#         print(main.get_stock(get_items,put_price))
#     elif choice=="view_stack":
#         print(f"stock in store is {main.view_stocks()}")
#     elif choice==" ":
#         start=False






    


            
        
