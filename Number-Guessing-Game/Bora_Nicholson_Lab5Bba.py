#Import Random Numberr
import random
#Define Guess
Guess = 0
#Def Main
def main():
    Number = random.randint(1,1000) #Random Number
    I=0
    Guess_Number = Guess_Again()
    while Guess_Number != Number:
        if Guess_Number > Number + 11:
            print ('Too High!')
            Guess_Number = Guess_Again()
            I= I+1
        elif Number + 11 > Guess_Number > Number:
            print ('Getting warm but still high!')
            Guess_Number = Guess_Again()
            I= I+1
        elif Number - 11 < Guess_Number < Number:
            print ('Getting warm but still low!')
            Guess_Number = Guess_Again()
            I= I+1
        elif Guess_Number < Number - 11:
            print ('Too low!')
            Guess_Number = Guess_Again()
            I= I+1
    else:
        print ('You guessed the number in' , I, 'tries!')
        Again = input('Do you want to try agian? Press y to play again: ')
        if Again == 'y':
            return main()

def Guess_Again():
    Guess = int(input('Guess a number: '))
    print ('The number you guessed is: ', Guess)
    return Guess

main()
