class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def update_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

    def get_marks(self):
        return self.__marks


student = Student("Rahul", 75)

student.update_marks(88)

print("Student:", student.name)
print("Marks:", student.get_marks())
