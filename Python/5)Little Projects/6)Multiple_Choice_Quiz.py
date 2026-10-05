from Question import Question

question_prompts = [
    "what colour are apples ?\n(a) red/green \n(b) yellow \n(c) black\n\n",
    "what colour are bananas ?\n(a) red/green \n(b) yellow \n(c) black\n\n",
    "what colour are blackberry ?\n(a) red/green \n(b) yellow \n(c) black\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        print(f"You got {score}/{len(questions)} correct")

run_test(questions)           