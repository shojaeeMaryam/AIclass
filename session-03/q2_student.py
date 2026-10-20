class Student:
    def init(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, course, grade):
        if 0 <= grade <= 20:
            self.grades[course] = grade
        else:
            print("Invalid grade")

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def best_course(self):
        if len(self.grades) == 0:
            return None
        return max(self.grades, key=self.grades.get)

    def failed_courses(self):
        failed = []
        for course in self.grades:
            if self.grades[course] < 10:
                failed.append(course)
        return failed

    def status(self):
        avg = self.average()
        if avg >= 17:
            return "Excellent"
        elif avg >= 14:
            return "Good"
        elif avg >= 12:
            return "Normal"
        else:
            return "Probation"

    def report(self):
        print(f"Student: {self.name} (ID: {self.student_id})")
        for course in self.grades:
            print(f"{course}: {self.grades[course]}")
        print(f"Average: {self.average()}")
        print(f"Best course: {self.best_course()}")
        print(f"Failed courses: {self.failed_courses()}")
        print(f"Status: {self.status()}")


class Classroom:
    def init(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def top_student(self):
        if len(self.students) == 0:
            return None
        top = max(self.students, key=lambda s: s.average())
        return top.name

    def class_average(self):
        if len(self.students) == 0:
            return 0
        total = 0
        for s in self.students:
            total = total + s.average()
        return total / len(self.students)


sara = Student("Sara Ahmadi", 40312345)
sara.add_grade("Math", 18)
sara.add_grade("Physics", 9)
sara.add_grade("Programming", 20)
sara.add_grade("English", 15)
sara.add_grade("Chemistry", 25)
sara.report()

ali = Student("Ali", 123)
ali.add_grade("Math", 12)
ali.add_grade("Physics", 15)
ali.report()

my_class = Classroom()
my_class.add_student(sara)
my_class.add_student(ali)
print("Top Student:", my_class.top_student())
print("Class Average:", my_class.class_average())

