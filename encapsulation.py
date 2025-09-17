# objective: create a student class that safely manage a student's information,ensuring that grade is always within a valid range of 0 and 100

class Student():
    def __init__(self,name,student_id):
        self.__name=name
        self.__student_id=student_id
        self.__grade=0

    def setgrade(self,grade):
        if 0<grade<100:
            self.__grade+=grade
        else:
            return "value should in between 0 and 100"
        
    def display_user(self):
        print(f"name:{self.__name} \nstudent_id:{self.__student_id} \ngrade:{self.__grade}")

    


student1=Student("srujan","1234")
student1.setgrade(60)
student1.display_user()

