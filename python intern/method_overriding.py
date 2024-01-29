class Animal:
    def sound(self):
        print("Animals making sound!!")
    def eat(self):
        print("Animals eating!!")
        
class Lion(Animal):       #inheritance
    def sound(self):       #method overriding
        print("Lion Roaring!!")

class Tiger(Animal):
    def sound(self):        #method overriding
        print("Tiger growls!!")
        
class Cat(Animal):          #inheritance
    def souund(self):
        print("Cat meows!!")

obj1 = Animal()
obj2 = Lion()
obj3 = Tiger()
obj4 = Cat()
obj1.sound()
obj1.eat()
obj2.sound()
obj2.eat()
obj3.sound()
obj4.sound()