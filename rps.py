# Name: Ibrahim Stamili
# Section: N/A
# Date: 29/9/2016
# rps.py

print "********** Exercise 2.1 **********"

print '\nRock, Paper, Scissors'


def get_input():
    input = raw_input('choice? ')
    # check if input is valid
    input = input.lower()
    if check_input(input):
        return input
    else:
        print 'This is not a valid object selection'


def check_input(choice):
    if choice == 'rock' or choice == 'paper' or choice == 'scissors':
        return True
    else:
        return False


def check_result(p1_choice, p2_choice):
    if p1_choice == p2_choice:
        print 'It\'s a draw'
    else:
        if p1_choice == 'rock':
            if p2_choice == 'scissors':
                print 'Player 1 wins - rock beats scissors'
            else:
                print 'Player 2 wins - paper beats rock'

        elif p1_choice == 'paper':
            if p2_choice == 'rock':
                print 'Player 1 wins - paper beats rock'
            else:
                print 'Player 2 wins - scissors beats paper'

        else:
            if p2_choice == 'paper':
                print 'Player 1 wins - scissors beats paper'
            else:
                print 'Player 2 wins - rock beats scissors'


def main():
    input_valid = False
    while not input_valid:
        print '\nPlayer 1'
        p1_choice = get_input()
        input_valid = check_input(p1_choice)

    input_valid = False
    while not input_valid:
        print '\nPlayer 2'
        p2_choice = get_input()
        input_valid = check_input(p2_choice)

    check_result(p1_choice, p2_choice)


main()