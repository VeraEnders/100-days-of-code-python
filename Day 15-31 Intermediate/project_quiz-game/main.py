from question import Question
from data import question_data
from game_brain import QuizBrain

question_bank = [Question(question["text"], question["answer"]) for question in question_data]

quiz = QuizBrain(question_bank)

while quiz.has_questions():
  quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score} / {quiz.question_number}.")