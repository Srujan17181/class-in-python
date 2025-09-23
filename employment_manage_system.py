# Use inheritance to model different types of employees in a company.


class Employee():
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def details(self):
        return f"name:{self.name}| id:{self.id} | salary:{self.salary}"
    

class Manager(Employee):
    def __init__(self,department,team_size,name,id,salary):
        super().__init__(name,id,salary)
        self.departments=department
        self.team_size=team_size
        

    def details(self):

        return f"{super().details()}\n {self.departments}| {self.team_size}"
    
class Developer(Employee):
    def __init__(self,programming_lang,experience,name,id,salary):
        super().__init__(name,id,salary)
        self.program=programming_lang
        self.exp=experience
    
    def details(self):
        return f"{super().details()} \n {self.program} | {self.exp}"


employ1=Manager("DEvops","10","srujan","145","125000")
print(employ1.details())

developer=Developer()