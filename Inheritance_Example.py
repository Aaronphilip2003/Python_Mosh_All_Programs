class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


bruno=Dog()
bruno.walk()

whiskers=Cat()
whiskers.walk()