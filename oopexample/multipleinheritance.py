class father:

    def father_character(self):
        print("Disciplined")


class mother:

    def mother_character(self):
        print("Caring")


class child(father, mother):
    pass


c = child()

c.father_character()
c.mother_character()
