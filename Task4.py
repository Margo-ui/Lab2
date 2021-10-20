class Student:
    def __init__(self, name, surname, rbnumber, grades):
        self.name = name
        self.surname = surname
        self.rbnumber = rbnumber
        self.grades = grades

    def average(self):
        avg = 0
        for number in self.grades:
            avg += number
        return avg / len(self.grades)


def takeSecond(elem):
    return elem[1]


class Group:
    def __init__(self):
        self.students = list()
        self.grades = list()

    def calc(self):
        for student in self.students:
            self.grades.append((student, student.average()))
        self.grades.sort(key=takeSecond, reverse=True)

    def printt(self):
        for student in self.grades[0:5]:
            print(student[0].name)
            print(student[1])


first = Student('ben', 'smith', 9, {1, 2, 3})
second = Student('alex', 'smithh', 8, {1, 2, 4})
third = Student('penny', 'smithg', 7, {1, 2, 5})
fourth = Student('sam', 'meow', 6, {1, 12, 3})
fifth = Student('george', 'jones', 5, {1, 2, 55})
sixth = Student('ann', 'ratto', 3, {9, 2, 3})
group = Group()
group.students = (first, second, third, fourth, fifth, sixth)
group.calc()
group.printt()
