

class student:
    college = 'xyz'  # class variables shared by the instances of the class

    def __init__(self, name, dept, year):
        self.name = name
        self.dept = dept
        self.year = year

    def display_info(self):
        print('Name of student {}'.format(self.name))
        print('Name of the department {}'.format(self.dept))
        print('Year studying {}'.format(self.year))
        print('College Studying {}'.format(student.college))


s1 = student('sheldon', 'physics', 3)
s2 = student('george', 'economics', 4)

s1.display_info()
print("*" * 50)
s2.display_info()