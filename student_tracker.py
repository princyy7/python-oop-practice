class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"{self.name}: added grade {grade}")
        else:
            print("Grade must be between 0 and 100.")

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def highest_grade(self):
        if len(self.grades) == 0:
            return None
        return max(self.grades)

    def lowest_grade(self):
        if len(self.grades) == 0:
            return None
        return min(self.grades)

    def is_passing(self):
        return self.average_grade() >= 40

    def show_report(self):
        avg = self.average_grade()
        high = self.highest_grade()
        low = self.lowest_grade()
        status = "PASS" if self.is_passing() else "FAIL"

        print(f"\nReport for {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average: {avg:.2f}")
        print(f"Highest: {high}")
        print(f"Lowest: {low}")
        print(f"Status: {status}")


# Test
s1 = Student("Princy")
s1.add_grade(75)
s1.add_grade(60)
s1.add_grade(35)
s1.show_report()

s2 = Student("Alex")
s2.add_grade(20)
s2.add_grade(30)
s2.show_report()
