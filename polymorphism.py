"Nossa super class se chama polymorphism"

#Super class
class Polymorphism:
    def __init__(self, name, is_id):
        self.name = name
        self.is_id = is_id

        "Nada esta privado, uma observaçao"

    # Method the super class
    def print_id(self):
        print(f"Your ID is - {self.is_id}")
    #Method the super class
    def your_Age(self, age):
        print(f"Your age is {age}")

#Sub class
class Child(Polymorphism):
    def __init__(self, name, age, ident):
        # Call the parent class constructor, passing the required arguments
        super().__init__(name, is_id=ident)
        self.age = age


def main():

