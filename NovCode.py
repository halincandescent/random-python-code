## mental math ##
import math
import random

def chooseLevel():
    # level 1,2,3
    ### ##### INDICE ISSUE 
    level = ['1','2','3']
    indice = random.randrange(0,2) # not including 3 yet 
    return level[indice] 

def chooseQuestion(level):
    # 1,2,3,4
    #### ##### INDICE ISSUE  
    questionId = ['1','2','3','4']
    indice = random.randrange(0,3) # not including 4 (division) yet 
    qID = questionId[indice]
    print('this is qID : ' + qID)
    if qID== '1':
        return additionProblem(level)
    elif qID== '2':
        return subtractionProblem(level)
    elif qID=='3':
        return multiplicationProblem(level)
    elif qID=='4':
        return divisionProblem(level)
    else:
        pass
    
def additionProblem(level):
    if level=='1':
        numberOne = random.randrange(0,10)
        numberTwo = random.randrange(0,10)
        question = str(numberOne)+' '+'+'+' '+str(numberTwo)+' = ' 
        answer = numberOne + numberTwo
        return question,answer
    elif level=='2':
        numberOne = random.randrange(0,100)
        numberTwo = random.randrange(0,100)
        question = str(numberOne)+' '+'+'+' '+str(numberTwo)+' = ' 
        answer = numberOne + numberTwo
        return question,answer
    elif level=='3':
        numberOne = random.randrange(0,1000)
        numberTwo = random.randrange(0,1000)
        question = str(numberOne)+' '+'+'+' '+str(numberTwo)+' = ' 
        answer = numberOne + numberTwo
        return question,answer    
    else:
        pass
        
def subtractionProblem(level):
    if level=='1':
        numberOne = random.randrange(0,10)
        numberTwo = random.randrange(0,10)
        question = str(numberOne)+' '+'-'+' '+str(numberTwo)+' = '
        answer = numberOne - numberTwo
        return question,answer
    elif level=='2':
        numberOne = random.randrange(0,100)
        numberTwo = random.randrange(0,100)
        question = str(numberOne)+' '+'-'+' '+str(numberTwo)+' = '
        answer = numberOne - numberTwo
        return question,answer
    elif level=='3':
        numberOne = random.randrange(0,1000)
        numberTwo = random.randrange(0,1000)
        question = str(numberOne)+' '+'-'+' '+str(numberTwo)+' = '
        answer = numberOne - numberTwo
        return question,answer
    else:
        pass 
        

def multiplicationProblem(level):
    if level=='1':
        numberOne = random.randrange(0,10)
        numberTwo = random.randrange(0,10)
        question = str(numberOne)+' '+'X'+' '+str(numberTwo)+' = '
        answer = numberOne*numberTwo
        return question,answer
    elif level=='2':
        numberOne = random.randrange(0,100)
        numberTwo = random.randrange(0,100)
        question = str(numberOne)+' '+'X'+' '+str(numberTwo)+' = '
        answer = numberOne*numberTwo
        return question,answer
    elif level=='3':
        numberOne = random.randrange(0,1000)
        numberTwo = random.randrange(0,1000)
        question = str(numberOne)+' '+'X'+' '+str(numberTwo)+' = '
        answer = numberOne*numberTwo
        return question,answer
    else:
        pass

def divisionProblem(level):
    ## a few issues 
    if level=='1':
        numberOne = random.randrange(0,10)
        numberTwo = random.randrange(0,10)
        question = str(numberOne)+' '+'/'+' '+str(numberTwo)+' = '
        answer = numberOne//numberTwo
        return question,answer
    else:
        pass 

def run():
    level = chooseLevel()
    question,answer = chooseQuestion(level)
    userAnswer = input(question)
    if float(userAnswer)==float(answer):
        print('yes')
    else:
        print('no')

## try and except statements
        
## turn it into a class that that retrieve certain diagnostics, like options
## for the answer to be shown if the question is wrong or for the questio to
## repeat if it's gotten wrong. or for options for it to constantly
## repeat or there are many different ways it can go



