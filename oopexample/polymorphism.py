class dog:

    def sound(self):
        print("bow bow")

class cat:

    def sound(self):
        print("meow")

def makesound(animal):
    animal.sound()

c = cat()
d = dog()
makesound(d)
makesound(c)