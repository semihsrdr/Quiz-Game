score=0
from data import question_data
def get_question(question):
    print("Q."+str(question.question_number+1)+":",question.question,"(True or False) :")
def check_answer(question,answer):
    if answer.capitalize()==question.answer:
        global score
        score+=1
        print("You got it right!")
        print("The correct answer was :",question.answer)
        print("Your current score is :",str(score)+"/"+str(question.question_number+1))
    elif answer.capitalize()!=question.answer:
        print("You got it wrong!")
        print("The correct answer was :", question.answer)
        print("Your current score is :", str(score) + "/" + str(question.question_number + 1))

    print()
    print()