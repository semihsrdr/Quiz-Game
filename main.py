from data import question_data
from quiz_brain import get_question,score,check_answer
from question_model import Question

question_number=0
while question_number<question_data.__len__():


    current_question=question_data[question_number].get("text")
    current_answer=question_data[question_number].get("answer")
    question=Question(current_question,current_answer,question_number)

    get_question(question)
    user_answer=input()
    check_answer(question,user_answer)
    question_number+=1





