# instance method
class Cart:   
    def __init__(self):
        self.items = {} 
    def add_item(self, item_name,quantity): 
        self.items[item_name] = quantity 
    def display_items(self):   
        print(self.items) 
a = Cart()
a.add_item("book", 3)
a.display_items()
#2nd ex
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def show(self):
        print('Name:', self.name, 'Age:', self.age)
 
p = Student("pradeep", 25)
p.show()
m = Student("ram", 30)
m.show()
#example of satic method
class employee:
    @staticmethod
    def sample(x):
        print("Inside static method", x)
 
employee.sample(10)
emp = employee()
emp.sample(10)
 
#2nd ex
class auth:
    @staticmethod
    def validate_password(password):
        if len(password) <6:
            return False
        else:
            return True
       
is_valid = auth.validate_password("welcome123")
print("password is valid : ", is_valid)
#class method example
class Student:
    school_name = 'zphs'
    def __init__(self, name, rool_no):
        self.name = name
        self.roll_no = rool_no
 
    @classmethod
    def change_school(cls, school_name):
        cls.school_name = school_name
    def show(self):
        print(self.name, self.roll_no, 'School:', Student.school_name)
 
st_1 = Student('pradeep', 24)
st_1.show()
Student.change_school('chaitanya')
st_1.show()
 
#example 2
class Pets:
    totalprice=10000
    @classmethod
    def m(cls,dog,cat,bird):
        cls.shopname="PETS STORE"
        print(dog)
        print(cat)
        print(bird)
        print(Pets.totalprice)
        print(cls.shopname)
 
animals=Pets()
animals.m("shitzu","bluecat","swift")

# '''The basic difference between the class method vs Static method 
# A class method takes class as the first parameter while a static method needs no specific parameters.
# A class method can access or modify the class state while a static method can’t access or modify it.
# In general, static methods know nothing about the class state. They are utility-type methods
# that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
# We use @classmethod decorator to create a class method and we use @staticmethod decorator to create a static method
# static method:-  static method does not require an instance of the class to be called and cannot access
# or modify the class state. Static methods are used when some functionality relates to the class
# but does not need any instance to perform the work
# To define a static method, you can use the @staticmethod decorator
# class method:- To create a class method, we use the @classmethod decorator or the classmethod()
# function. The method should take cls as its first parameter, which refers to the class itself.
