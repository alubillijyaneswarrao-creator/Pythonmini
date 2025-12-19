questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
score = 0
for i in range(len(questions)):
    print(questions[i])
    for option in options[i]:
        print(option)
    user_answer = input("Enter your answer (A/B/C/D): ").upper()
    if user_answer == answers[i]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {answers[i]}.\n")

print(f"Your final score is {score}/{len(questions)}")
