
"""
This examples is about instance variable and instance methods
They are nothing but the properties andn functions of the object
"""

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        print(self.first + ' ' + self.last)


emp_1 = Employee('suresh', 'ezhumalai', 5000)
emp_2 = Employee('test', 'user', 6000)

emp_1.fullname()
emp_2.fullname()
# emp_1.first = "Suresh"
# emp_1.last = "Ezhumalai"
# emp_1.email = "Suresh.Ezhumalai@company.com"
# emp_1.pay = 50000
#
# emp_2.first = "Test"
# emp_2.last = "User"
# emp_2.email = "Test.User@company.com"
# emp_2.pay = 6000

# print(emp_1.email)
# print(emp_2.email)
