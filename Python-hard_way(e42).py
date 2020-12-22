class animal(object):
    pass

class dog(animal):
    def __init__(self,name):
        self.name = name

class cat(animal):
    def __init__(self,name):
        self.name = name

class person(object):
    def __init__(self,name):
        self.name = name
        self.pet = None

class employee(person):
    def __init__(self, name, salary):
        super(employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass
class Salmon(Fish):
    pass
class Halibut(Fish):
    pass

rover = dog("Rover")
satan = cat("Satan")
mary = person("Mary")
mary.pet = satan
frank = employee("Frank", 120000)
frank.pet = rover
flipper = Fish()
crouse = Salmon()
harry = Halibut()