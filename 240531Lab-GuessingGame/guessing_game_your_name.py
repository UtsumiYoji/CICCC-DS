import random

def main():
    lower = 1
    upper = 1000
    correct_numer = random.randint(lower, upper)
    guess_count = 0

    low = 1
    up = 1000

    while True:
        # get number from user
        while True:
            usr_ipt = input('Enter your guess from ' + str(low) + ' to ' + str(up) + ': ')
            if not usr_ipt.isdecimal():
                print('You can input only postive number, input again')
                continue

            usr_ipt = int(usr_ipt)
            if not low < usr_ipt < up:
                print('You can input from ' + str(low) + 'to' + str(up) + ', input again')
                continue

            break

        # make sure it is correct
        if usr_ipt == correct_numer:
            print('You got it! The hidden number is ' + str(correct_numer))
            break

        # if it is wrong
        guess_count += 1
        print('Wrong! Guess count:', guess_count)

        # set next range
        if correct_numer > usr_ipt:
            low = usr_ipt + 1
        else:
            up = usr_ipt - 1

if __name__ == '__main__':
    main()