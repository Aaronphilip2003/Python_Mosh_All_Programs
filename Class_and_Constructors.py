class Person:#class
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f'Hello my name is {self.name}')


aaron=Person("Aaron")
john=Person("John")
print (aaron.talk())
print(john.talk())