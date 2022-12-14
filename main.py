from data import question_data
from question_model import Question
from quizbrain_model import QuizBrain

question_bank = []

for combo in question_data:
    temp = Question(combo['question'], combo['correct_answer'])
    question_bank.append(temp)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.game_end()