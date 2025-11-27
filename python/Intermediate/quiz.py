quiz = {
    "What is the capital of France? ": "Paris",
    "Who painted the Mona Lisa? ": "Leonardo da Vinci",
    "What is the largest planet in our solar system? ": "Jupiter",
    "Who is known as the father of computers? ": "Charles Babbage",
    "What is the smallest prime number? ": "2",
    "Which element has the chemical symbol 'O'? ": "Oxygen",
    "Who discovered gravity? ": "Isaac Newton",
    "What is the national animal of India? ": "Tiger",
    "In which year did World War II end? ": "1945",
    "Which is the longest river in the world? ": "Nile"
}
score = 0
for question, answer in quiz.items():
    print("Question:", question)
    user_input = input("Enter the answer: ")
    input_lower_trim = user_input.strip().lower()
    if answer.lower().strip() == input_lower_trim:
        print("Your answer is right!")
        score += 1
    else:
        print("Sorry, wrong answer")
    print(f"Your score is: {score}")

print(f"Final score is: {score}/{len(quiz)}")
