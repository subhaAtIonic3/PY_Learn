class Dog():
    # Class object attribute
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self):
        print(f"WOOF! My name is {self.name}")

    def speak_number(self, number):
        for _ in range(0, number):
            print("WOOF!!")


coco = Dog(breed="Lab", name="Coco")

print(type(coco))
print(coco.name)
print(coco.species)
print(coco.bark())
print(coco.speak_number(4))


class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = Circle.pi * (radius ** 2)

    def get_circumference(self):
        return self.radius * Circle.pi * 2


my_circle = Circle(radius=4)
print(my_circle.get_circumference())
print(my_circle.area)


class Animal():

    def __init__(self):
        print("Animal created")

    def eat(self):
        print("I am eating")

    def who_am_i(self):
        print("I am an animal")


class Human(Animal):

    def __init__(self, name):
        super().__init__()
        self.name = "Subha"

    def who_am_i(self):
        print(f"My name is {self.name}")


subha = Human(name="Subha")
subha.who_am_i()
subha.eat()

# Polymorphism


class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"


class Cow():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says mow!"


niko = Cow(name="Niko")
felix = Cat(name="Felix")

print(niko.speak())
print(felix.speak())


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)


class Vehicle():
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    def show_manufacturer(self):
        raise NotImplementedError(
            "Subclass must implemented this absstract method")


class Bmw(Vehicle):

    def show_manufacturer(self):
        return "Made by " + self.manufacturer


class Audi(Vehicle):

    def show_manufacturer(self):
        return "Made by " + self.manufacturer


bmw = Bmw(manufacturer="BMW")
audi = Audi(manufacturer="AUDI")

print(bmw.show_manufacturer())
print(audi.show_manufacturer())
