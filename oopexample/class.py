# example of class
# class is a way of binding data and functionality together. It provides a basic blueprint from which
# n number of instances can be created

class person:

    def __init__(self, name):
        self.name = name

    def display(self):
        print('hello {}'.format(self.name))


p = person('suresh')
p.display()


# print(p)
