class Questions:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self. answer = answer

class QuizGame:
    def __init__(self):
        self.questions = []
        self.score = 0
    
    def add_questions(self,question):
        self.questions.append(question)
    
    def start(self):
        print("Welcome to the quiz game!")
        print("-------------------------")
        for idx,question in enumerate(self.questions, start =1):
            user_answer = input(f"Q{idx}: {question.prompt}")
            if user_answer.strip().lower() == question.answer.lower():
                print("Correct!")
                self.score +=1
            else:
                print(f"Wrong anser, correct answer is {question.answer} ")
        
        print(f"Quiz over, Your final score is {self.score}/{len(self.questions)} ")

        





question_promt = [
"What is the capital of France? ",
"2 + 2 = ? ",
"What is the color of the sky? "
]

answers = ["Paris", "4", "Blue"]

quiz = QuizGame()
for prompt, answer in zip(question_promt, answers):
    quiz.add_questions(Questions(prompt, answer))

quiz.start()