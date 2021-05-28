"""
Class methods used to set values for the class variables
Also it can be used as alternative constructor
"""

"""
static methods doesnot belong to instance or class methods. but it does have a logical relationship
with the class
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

    @classmethod
    def set_raise_amt(cls, raise_amount):
        cls.raise_amount = raise_amount

    @classmethod
    def fromstring(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_work_day(day):

        if day in [1, 2, 3, 4, 5]:
            return True
        else:
            return False



emp1 = Employee('test1', 'user1', 5000)
print(emp1.raise_amount)
emp1.set_raise_amt(1.05)
print(emp1.raise_amount)

emp2 = Employee.fromstring('test2-user2-20000')
print(emp2.first)
print(emp2.last)
print(emp2.pay)

print(emp2.is_work_day(1))