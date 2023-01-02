from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i["question"], i["correct_answer"]))
    # print(f"Creating question: {i['text']}\n and then the answer: \n {i['answer']}")

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz!\n"
      f"Your final score was {quiz.score}/{len(quiz.questions_list)}")

