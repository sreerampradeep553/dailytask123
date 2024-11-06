#nested class:- block inside another block is called nested block


class human:
    def __init__(self,name,age,skill):
        self.name = name
        self.age = age
        self.skill = skill
    
    def display(self):
        print(self.name)
        print(self.age)
        print(self.skill)
    
    class human:
        def __init__(self,salary,domain):
            self.salary = salary
            self.domain = domain
        def display(self):
            print(self.salary)
            print(self.domain)
    
    m = human(45000,"driver")
    m.display()

p = human("teja",30,"driver")
p.display()