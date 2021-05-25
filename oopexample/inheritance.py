# accessing the attributes of the base class by a derived class

class animal:

    def eating(self):
        print("eating")


class dog(animal):

    def barking(self):
        print("barking")

d = dog()
d.eating()
d.barking()