
# Enter name: 

import random

targetWord = "T"

def monkeys_typing():
    guessNumber = random.randint(65, 90)
    letter1 = chr(guessNumber)
    count = 1
    guess = letter1
    print(guess)

    while guess != targetWord:
        guessNumber = random.randint(65, 90)
        letter1 = chr(guessNumber)
        guess = letter1
        print(guess)
        count +=1 
    
    return count

print(monkeys_typing())