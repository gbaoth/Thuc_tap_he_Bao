class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def GetName(self):
        return self.name
    def SelectDataForPrint(self):
        pass
    def Print(self):
        print(self.SelectDataForPrint())

class ScienceStudent(Student):
    def SelectDataForPrint(self):
        return self.age

    def Print(self):
        print("The student whose name is %s is %d years old" % (self.name,self.SelectDataForPrint()))

StudentA = ScienceStudent("Bao", 18, "Saigon")
StudentA.Print()