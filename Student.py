class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def GetName(self):
        print("The student's name is: %s" % self.name)
    def SelectDataForPrint(self):
        pass
    def Print(self):
        print(self.SelectDataForPrint())

class ScienceStudent(Student):
    def SelectDataForPrint(self):
        return "%d" % self.age

    def Print(self):
        print("The student is %s years old" % self.SelectDataForPrint())

StudentA = ScienceStudent("Bao", 18, "Saigon")
StudentA.Print()