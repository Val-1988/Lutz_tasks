class Animal:
    def reply(self):
        self.speak()

    def speak(self):
        print("go down")

        
class Mammal(Animal):
    pass


class Cat(Mammal):
    def speak(self):
        print("mya")


class Dog(Mammal):
    def speak(self):
        print("gaw")


class Primat(Mammal):
    def speak(self):
        print("u-u-u-u == Hello world")


class Hacker(Primat):
    pass
