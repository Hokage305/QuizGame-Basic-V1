
#This allows the program to run a script for the quiz game
#The code above utilizes the function "def" and "for" statements
#The "for" statement is used to string the sequences together
#The "if" statement is used for conditional execution.
#Basically a "Boolean" operation to identify what's true or false.
#These lines run for every question also


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

# List of quiz questions. Each question is a dictionary.
#Modifiable depending on if you want to add or subtract questions/answers.
questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    }
]

# Run the quiz
run_quiz(questions)