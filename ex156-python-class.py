class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello my name is {self.name} and I am {self.age} old.")

Alice = Person("Alice", 30)

Alice.say_hello()