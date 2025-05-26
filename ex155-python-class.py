class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"Meow! Mon nom est {self.name}.")

mon_chat = Cat("Fluffy")

mon_chat.meow()