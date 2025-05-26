class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):
        self.grades.append(grade)

    def display_grades(self):
        print(f"Notes de {self.name}: {self.grades}")

    def average_grade(self):
        avg = round(sum(self.grades) / len(self.grades), 2)
        #print(f"Moyenne des notes : {avg}")
        return avg

class Course:
    def __init__(self, name, students=[]):
        self.name = name
        self.students = students

    def add_student(self, student: Student):
        self.students.append(student)

    def display_students(self):
        print(f"Étudiants inscrits au cours {self.name}:")
        for student in self.students:
            #print(f"{student.name}: {student.grades}")
            print(f"{student.name}")

    def best_student(self):
        best_student = None
        best_moyenne = 0
        for student in self.students:
            if (student.average_grade() > best_moyenne):
                best_student = student
        print(f"{best_student.name}")

    def students_above_average(self):
        for student in self.students:
            if (student.average_grade() > 13):
                print(student.name)

    def rank_students(self):
        ranked_students = sorted(self.students, key=lambda student: student.average_grade(), reverse=True)
        for i, student in enumerate(ranked_students, start=1):
            avg = student.average_grade()
            print(f"{student.name} {avg}")

    def average_course_grade(self):
        all_grades = []
        for student in self.students:
            for grade in student.grades:
                all_grades.append(grade)

        total_avg = round(sum(all_grades) / len(all_grades), 2)
        print(f"Moyenne générale du cours {self.name} : {total_avg}")

    def remove_student(self, student: Student):
        self.students.remove(student)

    def rename_student(self, name, student: Student):
        student.name = name
        self.display_students()

alice = Student("Alice")
alice.add_grade(14)
alice.add_grade(13)
#alice.display_grades()
#alice.average_grade()
bob = Student("Bob")
bob.add_grade(18)
bob.add_grade(12)
charlie = Student("Charlie")
charlie.add_grade(14)
charlie.add_grade(14)
python_course = Course("Python")
python_course.add_student(alice)
python_course.add_student(bob)
python_course.add_student(charlie)
#python_course.display_students()
#python_course.best_student()
#python_course.students_above_average()
#python_course.rank_students()
#python_course.average_course_grade()
#python_course.remove_student(bob)
#python_course.display_students()
python_course.rename_student("Alicia", alice)
