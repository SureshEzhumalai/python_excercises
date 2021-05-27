"""
It is the way of wrapping data and functions together.
Private variables and private methods are the examples of encapsulation in python
"""


class car:
    __max_speed = 0
    __color = ""

    def __init__(self):
        # self.__updatesoftware()
        self.__max_speed = 150
        self.__color = "black"

    def drive(self):
        print("driving")
        print("max speed is {}".format(self.__max_speed))

    def __updatesoftware(self):
        print("updating software")

    def setSpeed(self):
        self.__max_speed = 100
        print("max speed is {}".format(self.__max_speed))


c = car()
c.drive()
c.setSpeed()
