class Animal:
    def __init__(self, name, privateAttribute):

        self.name = name
        self.__privateAttribute = privateAttribute

    def speak(self):
        return f"{self.name} speaks"

    def privAtt(self):
        return f"{self.__privateAttribute} is a {self.name}'s private attribute"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says howhow"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow meow"


cat = Cat("kitty", "nose")
dog = Dog("jack", "leg")
print(cat.speak())
print(dog.speak())
print(cat.privAtt())
