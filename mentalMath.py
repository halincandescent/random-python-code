import math
import random

class mathQuestion:

    def __init__(self):
        self.question = None
        self.answer = None
        self.level = None

    def chooseLevel(self):
        # level 1,2,3
        ### ##### INDICE ISSUE 
        level = ['1','2','3']
        indice = random.randrange(0,2) # not including 3 yet 
        return level[indice]     

    def chooseQuestion(self,level):
        # 1,2,3,4
        #### ##### INDICE ISSUE  
        questionId = ['1','2','3','4']
        indice = random.randrange(0,3) # not including 4 (division) yet 
        qID = questionId[indice]
        if qID== '1':
            return self.additionProblem(level)
        elif qID== '2':
            return self.subtractionProblem(level)
        elif qID=='3':
            return self.multiplicationProblem(level)
        elif qID=='4':
            return self.divisionProblem(level)
        else:
            pass

    def additionProblem(self,level):
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
        
    def subtractionProblem(self,level):
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
        

    def multiplicationProblem(self,level):
        if level=='1':
            numberOne = random.randrange(0,10)
            numberTwo = random.randrange(0,10)
            #question = str(numberOne)+' '+'X'+' '+str(numberTwo)+' = '
            question ='  ' +str(numberOne)+' '+'\n'+'X '+str(numberTwo)+' = '
            answer = numberOne*numberTwo
            return question,answer
        elif level=='2':
            numberOne = random.randrange(0,100)
            numberTwo = random.randrange(0,100)
            #question = str(numberOne)+' '+'X'+' '+str(numberTwo)+' = '
            question ='  ' +str(numberOne)+' '+'\n'+'X '+str(numberTwo)+' = ' 
            answer = numberOne*numberTwo
            return question,answer
        elif level=='3':
            numberOne = random.randrange(0,1000)
            numberTwo = random.randrange(0,1000)
            question ='  ' +str(numberOne)+' '+'\n'+'X '+str(numberTwo)+' = '
            #question = str(numberOne)+' '+'X'+' '+str(numberTwo)+' = '
            answer = numberOne*numberTwo
            return question,answer
        else:
            pass

    def divisionProblem(self,level):
        ## a few issues 
        if level=='1':
            numberOne = random.randrange(0,10)
            numberTwo = random.randrange(0,10)
            question = str(numberOne)+' '+'/'+' '+str(numberTwo)+' = '
            answer = numberOne//numberTwo
            return question,answer
        else:
            pass 

    def run(self):
        level = self.chooseLevel()
        self.question,self.answer = self.chooseQuestion(level)
        userAnswer = input(self.question)
        if float(userAnswer)==float(self.answer):
            print('yes')
        else:
            print('no')
            print('answer is : ' + str(self.answer))

    def runMultiplication(self):
        level = self.chooseLevel()
        self.question,self.answer = self.multiplicationProblem(level)
        userAnswer = input(self.question)
        if float(userAnswer)==float(self.answer):
            print('yes')
        else:
            print('no')
            print('answer is : ' + str(self.answer))

if __name__=='__main__':
    game = mathQuestion()
    i = 0
    while i < 5: #5 turns
        game.runMultiplication()
        i = i + 1
    print('thanks for playing') 

    

    
