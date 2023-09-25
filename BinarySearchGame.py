import random

trials = 0
lb = 1
ub = 100
num = (lb + ub) // 2
question = ""


def numberQuestion(lb, ub, question, num):
    if question == "less":
        # global lb
        # global ub
        lb = lb
        ub = num - 1
    elif question == "more":
        lb = num + 1
        ub = ub
    if question != "equal":
        num = (lb + ub) // 2
    # print lb, ub
    return lb, ub, num;


def win(trials, num):
    if question == "equal" and trials <= 7:
        print
        "Your number is " + str(num)
        print
        "The computer won in " + str(trials) + " tries"


def lose():
    if trials > 7:
        print
        "You chose a number out of range or changed your number"
    else:
        print


# questionOne = input("Is your number more, less, or equal to 50: ")
# if questionOne == "more":
#    numberQuestion(50,100)
#
# elif questionOne == "less":
#    numberQuestion(0,50)

while question != "equal":
    question = input("Is you number more, less, or equal to " + str(num))
    lb, ub, num = numberQuestion(lb, ub, question, num)
    # numberQuestion(lb,ub)
    trials = trials + 1
    if lb > 100:
        print
        " Your number cannot be greater than 100."
        break
    if ub < 1:
        print
        "Your number cannot be less than 0"
        break
    # win(trials, number)
    if trials > 7:
        print
        "You chose a number out of range or changed your number"
        break
win(trials, num)
lose()

