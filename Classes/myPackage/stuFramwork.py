from student import students


class StudentFramework:
    students = []

    def add(self, id, fname, lname, std, mark, school):
        s1 = students(self, 100, "savan", "minsariya", 10, 100, "saint thomas school")
        self.students.append(s1)


print(students)