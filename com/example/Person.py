class Person:
    def __init__(self, fname, lname, gender):
        self.fname = fname
        self.lname = lname
        self.gender = gender

    def show_person(self):
        print("The person name is: ", self.fname+" "+self.lname+" and gender is: ", self.gender)


p = Person("Shakti", "Rath", "M")
p.show_person()
