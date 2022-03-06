import random, time, sys, string

guessed = False

class funcs:

    def digitguess(self):
        guessno = 0
        toguess = input('Enter a digit to guess >> ')
        if string.ascii_letters in toguess:
            print('You have to input a number!')

        elif int(toguess) > 10000:
            print('That will take too long to guess')
            input()
            funcs.digitguess()


        print(f'Attempting to guess {toguess}')
        
        length = len(toguess)


        
        while True:
            num = []
            for i in range(length):
                num.append(random.randint(0,9))
            num = str(num).replace("[", '').replace("]", '').replace("'", '').replace(",", '').replace(" ", '')
            
            
            if num == toguess:
                print(f'Guessed {num}, Worked')
                guess()
            else:
                guessno += 1
                print(f'Attempted {num}, Failed, GuessNO : {guessno}')

    def bforce(self):
        guessno = 0
        password = input('Enter a password ot guess >> ')

        for passw in open('trypass.txt', 'r'):
            if passw == password:
                print('Guessed Password')
                input()
            else:
                guessno = guessno +1
                print(f'Gusesed {passw}, Failed, GuessNO: {guessno}')
        print('failed')
        input()




funcs = funcs()
def guess():

    print('1 - digit brute force')
    print('2 - word brute force')

    try:

        opt = int(input('----> '))
    except:
        guess()

    

    if opt ==1:
        funcs.digitguess()

    elif opt ==2:
        funcs.bforce()

    else:

        print('Not an option')
        input()
        guess()

guess()