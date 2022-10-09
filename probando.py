def saludar():
    print("Hola!")

def publicidad():
    print("100.000 adena / 10 USD / PM me!")

def despedirse():
    print("Bueno chao.")

class Dog:
    id = 0

    def __init__(self, name):
        self.name =name

    def lick(self, person_name):
        print(f"{self.name} licks {person_name}. \"Lick Lick Lick\" *Lick* *Lick* *Lick*")