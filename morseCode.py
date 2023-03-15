morseDictionary = {
    "a" : '.-',
    "b" : '-...',
    "c" : '-.-.',
    "d" : '-..',
    "e" : '.',
    "f" : '..-.',
    "g" : '--.',
    "h" : '....',
    "i" : '..',
    "j" : '.---',
    "k" : '-.-',
    "l" : '.-..',
    "m" : '--',
    "n" : '-.',
    "o" : '---',
    "p" : '.--.',
    "q" : '--.-',
    "r" : '.-.',
    "s" : '...',
    "t" : '-',
    "u" : '..-',
    "v" : '...-',
    "w" : '.--',
    "x" : '-..-',
    "y" : '-.--',
    "z" : '--..',

    "1" : '.----',
    "2" : '..---',
    "3" : '...--',
    "4" : '....-',
    "5" : '.....',
    "6" : '-....',
    "7" : '--...',
    "8" : '---..',
    "9" : '----.',
    "0" : '-----'
}  

def lettersToMorse(message,morseDic):
    stringMorse = ''
    for letter in message:
        if letter.isspace():
            stringMorse = stringMorse + '/ '
        else:
            if letter in morseDic.keys():
                stringMorse = stringMorse + morseDic[letter] + ' ' 
        
    return stringMorse

def morseToLetters(message,morseDic):
    listMessage = message.split() 
    stringLetters = ''
    for code in listMessage:
        if code == '/':
            stringLetters = stringLetters + ' '
        else:
            for key in morseDic.keys():
                if code == morseDic[key]:
                    stringLetters = stringLetters + key
            
    return stringLetters

if __name__=='__main__':
    message = 'hello world'
    mc = lettersToMorse(message,morseDictionary)
    print(mc)
    morsecode = morseToLetters(mc,morseDictionary)
    print(morsecode)     
 
