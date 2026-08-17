"Nossa super class se chama polymorphism"

#Super class
class Polymorphism:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
        "Nada esta privado, uma observaçao"

    # Method the super class
    def print_id(self):
        print(f"Your ID is - {self.id}")

    def your_Age(self, age):
        print(f"Your age is {}")
