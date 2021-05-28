class Employee:

    raise_amount = 0 # class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first + '.' + self.last + '@company.com'
        self.pay = pay

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        return self.pay * self.raise_amount

    @classmethod
    def set_raise_amount(cls, raise_amount):
        cls.raise_amount = raise_amount


class Developer(Employee):

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self,first, last, pay, employee = None):
        super().__init__(first,last, pay)
        if employee == None:
            self.employee = []
        else:
            self.employee = employee


    def add_employee(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_employee(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def print_emp(self):
        for emp in self.employee:
            print('--->', emp.fullname())

emp1 = Employee('suresh', 'ezhumalai', 50000)
print(emp1.apply_raise())
emp1.set_raise_amount(1.05)
print(emp1.apply_raise())

emp2 = Developer('test', 'user', 60000, 'python')
print(emp2.fullname())
print(emp2.raise_amount)
print(emp2.apply_raise())

emp3 = Developer('test1', 'user1', 65000, 'java')

mgr_1 = Manager('george', 'cooper', 90000, [emp3])

mgr_1.add_employee(emp3)
mgr_1.add_employee(emp2)
mgr_1.remove_employee(emp2)
mgr_1.print_emp()