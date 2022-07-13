class Mammal:
    def walk(self):
        print("walk")


# inherit Mammal class
class Cat(Mammal):
    # prevent empty class warning
    pass


class Dog(Mammal):
    # def second method specific to this class
    def bark(self):
        print("bark")


dog = Dog()
dog.bark()
cat = Cat()
cat.walk()