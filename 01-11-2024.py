#'"1.Create a class Person that has instance variables name, age, and gender. Add methods to:
#Initialize these variables."
#Update the age.
#Display the persons" information."
#Exercise:
 #> Create multiple instances of the Person class.
 #> Change the age of one person and display the updated information."'


class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_gender(self):
        return self.gender
    
    def update_age(self,new_age):
        self.age=new_age

    def display_info(self):
        print(f"name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Gender:{self.gender}")


person1 = Person("Pradeep",24,"male")
person2 = Person("balaji",21,"male")
person3 = Person("jeshwin",4,"male")
person4 = Person("ramana",40,"male")

person1.display_info()
print()
person2.display_info()
print()
person3.display_info()
print()
person3.update_age(23)
print()
person3.display_info()
print()



#2.Create a class Company that keeps track of the total number of employees using a static variable total_employees. 
 # Each employee has instance variables name and department. Every time an employee is added, the total_employees should increment.
  #Exercise:
   #>Create multiple employee instances.
   #>Print the total number of employees after adding each new employee.
   #>Check whether changing the total_employees in one instance affects the others.


class Company:
    total_employees = 0

    def __init__(self,name,department):
        self.name = name
        self.department = department
        Company.total_employees +=1

    def display_info(self):
        print(f"Name:{self.name}")
        print(f"department:{self.department}")


    @classmethod
    def get_total_employees(cls):
        return cls.total_employees
    
    @classmethod
    def set_total_employees(cls,value):
        cls.total_employees = value


emp1= Company("pradeep","associate")
print("total Employees:",Company.get_total_employees())
emp2= Company("balaji","Associate")
print("total Employees:",Company.get_total_employees())



# 3.Create a class Rectangle that has instance variables length and width. 
#  Add a method calculate_area that calculates and prints the area of the rectangle using local variables inside the method.
#  Exercise:
#   >Create instances of the Rectangle class with different lengths and widths.
#   >Calculate and print the area for each rectangle.  


class Rectangle:
    def __init__ (self,length,width):
        self.length = length
        self.width = width
        
    def calculate_area(self,area):
        self.area  = area
        area = self.length * self.width
        print(f"Rectangle with length {self.length} and width {self.width} has an area of {area}square units.")

rect1 = Rectangle(5,3)
rect2 = Rectangle(10,5)
rect3 = Rectangle(8,4)
rect4 = Rectangle(20,10)

print("Rectangle Areas:")
rect1.calculate_area(1)
rect2.calculate_area(2)
rect3.calculate_area(3)
rect4.calculate_area(4)



#4.Create a class Employee where:
 # Each employee has an instance variable salary.
 # There is a static variable bonus shared by all employees. The bonus is applied to each employee's salary.
 # Write a method total_salary that calculates the total salary for an employee (including the bonus).
 # Exercise:
  # >Create several employee instances with different salaries.
  # >Change the bonus amount (static variable) and see how it affects all employees.
  # >Calculate and print the total salary for each employe


class Employee:
    bonus = 0.10
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def total_salary(self):
        return self.salary+(self.salary * Employee.bonus)
    
    def __str__(self):
        return f"{self.name}-salary:${self.salary:.2f},Bonus:{Employee.bonus*100}%,Total salary:${self.total_salary():.2f}"
    
emp1 =Employee("pradeep",50000)
emp2 =Employee("balaji",60000)
emp3 =Employee("jesh",70000)

print("initial Total Salaries:")
print(emp1)
print(emp2)
print(emp3)

    