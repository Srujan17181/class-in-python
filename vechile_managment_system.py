class Vehicle():
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def display_info(self):
        return f"brand:{self.brand}| model:{self.model}| year:{self.year}"
    

class car(Vehicle):
    def door_num(self,door_no):
        self.door_no=door_no

    def display_info(self):
        return super().display_info()

class truck(Vehicle):
    def payload_capacity(self,load):
        self.load=load

    def display_info(self):
        return super().display_info()
    
class motorcycle(Vehicle):
    def types(self,type):
        self.type=type

    def display_info(self):
        return super().display_info()
    

cars=car("BMW","A3","2004")
print(cars.display_info())