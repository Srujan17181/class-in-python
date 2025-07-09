
class question_list:
    def __init__(self,q_list):
        self.question_number=0
        self.score=0
        self.ques_list=q_list

    def still_have_question(self):
        return self.question_number < len(self.ques_list)
    
            
            


    def next_question(self):
        current_question=self.ques_list[self.question_number]
        self.question_number+=1
        user_answer=input(f'{self.question_number}:{current_question.text} :  (true/false): ')
        self.check_question(user_answer,current_question.answer)

    def check_question(self,user_answer,correctans):
        if user_answer.lower()==correctans.lower():
            self.score+=1
            print("you got it Right")
        else:
            print("wrong answer")
            print(f'te correct answer is {correctans}')
        print(f'your score is {self.score}/{self.question_number}')




      












