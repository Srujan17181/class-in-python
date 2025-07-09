import quizgame
import quizbrain
import data



        



questionbank=[]
for question in data.question_data:
    text_question=question['text']
    answer_question=question['answer']
    new_question=quizgame.Question(text_question,answer_question)
    questionbank.append(new_question)




quiz=quizbrain.question_list(questionbank)
while quiz.still_have_question():
    quiz.next_question()


