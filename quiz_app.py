class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer.lower().strip()


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        print("Welcome to the Quiz!\n")
        for i, q in enumerate(self.questions, start=1):
            user_answer = input(f"Q{i}. {q.prompt} ").lower().strip()
            if user_answer == q.answer:
                self.score += 1
                print("Correct!\n")
            else:
                print(f"Wrong. Correct answer: {q.answer}\n")

        self.show_result()

    def show_result(self):
        total = len(self.questions)
        percent = (self.score / total) * 100
        print(f"Final Score: {self.score}/{total} ({percent:.1f}%)")
        if percent >= 70:
            print("Result: PASS")
        else:
            print("Result: KEEP PRACTICING")


# Quiz data
questions = [
    Question("What is the keyword to define a class in Python?", "class"),
    Question("What method is called when an object is created?", "__init__"),
    Question("OOP stands for?", "object oriented programming"),
    Question("Which concept allows one class to use another class's features?", "inheritance"),
]

quiz = Quiz(questions)
quiz.run()
