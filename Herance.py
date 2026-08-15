#Super class
class Herance:
    def __init__(self, name, age, year):
        self._name = name
        self._age = age
        self.year = year
        #Definindo atriburos de classe para instaciar objetos

    def verificarIdade(self):
        if self._age >= 18:
            print("Vocẽ é maior de idade")
        else:
            print("Vocẽ é menor de idade")

# Sub class
