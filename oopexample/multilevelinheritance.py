"""
This is example is about multilevel inheritance
"""

class person:

    def display(self):
        print("This is the person class.")


class employee(person):

    def disp_info(self):
        print("this is the employee class")


class programmer(employee):

    def display_info(self):
        print("this is programmer class")

prg = programmer()

prg.display()
prg.disp_info()
prg.display_info()