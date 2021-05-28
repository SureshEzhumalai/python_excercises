"""
Class variables shared by all instances of the object
instance variables unique to each instance of the object
"""

class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        Employee.num_of_emps = Employee.num_of_emps + 1
    def fullname(self):
        print(self.first + ' ' + self.last)

    def apply_raise(self):
        return self.pay * self.raise_amount


emp_1 = Employee('suresh', 'ezhu', 50000)
emp_2 = Employee('Test', 'User', 60000)
emp_3 = Employee('Test1', 'User1', 35000)

emp_1.raise_amount = 1.05
# print(emp_1.__dict__)
# print(emp_2.__dict__)
# print(Employee.__dict__)

print(emp_1.apply_raise())

print(emp_2.apply_raise())

print(Employee.num_of_emps)