class QuizBrain:
    
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
        
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
           
           
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(answer, current_question.answer)
        
    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right! {self.score}/{self.question_number}")
        else:
            print(f"You got it wrong! {self.score}/{self.question_number}")
        print("\n")
        
    def game_end(self):
        print("You have completed the quiz!")
        print(f"Your final score was {self.score}/{self.question_number}")
            
        
        