import sys
import time
import random

wait = time.sleep


def start():
    print("Declare your starting money($)")
    money = int(sys.stdin.readline())
    prize = 0
    if money <= 0:
        print("Starting money must be greater than zero.")
        start()
    print("Want to know the rules? (1 - yes, 2 - skip)")
    rules_answer = int(sys.stdin.readline())
    if rules_answer == 1:
        rules()
        game(money, prize)
    elif rules_answer == 2:
        game(money, prize)
    else:
        print("Wrong input")
        start()


def rules():
    print("You play the dice game. Every round you are asked, how much money you want to bet.")
    wait(1)
    print("Then, you choose the risk. You can bet 1, 2 or 3 numbers from a 6-side dice.")
    wait(1)
    print("Greater the risk - greater the reward.")
    wait(1)
    print("If you choose 1 number - you get 6x your money as reward.")
    wait(1)
    print("If you choose 2 numbers - you get 3x your money as reward.")
    wait(1)
    print("If you choose 3 numbers - you get 2x your money as reward.")
    wait(1)
    print("That's all.")


def game(money, prize):
    money = money + prize
    if money <= 0:
        empty_account()
    print("You have %s$ on your account." % money)
    wait(1)
    print("How much money do you want to bet on this round?($)")
    round_money = int(sys.stdin.readline())
    if round_money > money:
        print("You cannot bet more than you have. Try again.")
        money = money - prize
        game(money, prize)
    money = money - round_money
    numbers_choice(money, prize, round_money)


def numbers_choice(money, prize, round_money):
    print("How many numbers do you want to choose? (1, 2 or 3)")
    round_numbers = int(sys.stdin.readline())
    if round_numbers == 1:
        one_number(round_money, money)
    elif round_numbers == 2:
        two_numbers(round_money, money)
    elif round_numbers == 3:
        three_numbers(round_money, money)
    else:
        print("Incorrect number. Try again.")
        numbers_choice(money, prize, round_money)


def one_number(round_money, money):
    print('Choose your number(1-6)')
    first_number = int(sys.stdin.readline())
    if first_number <= 0 or first_number > 6:
        print("Wrong number has been chosen. Select a number from range 1 to 6.")
        one_number(round_money, money)
    money_multiplier = 1
    numbers = [first_number]
    round(numbers, money_multiplier, round_money, money)


def two_numbers(round_money, money):
    print("Choose your first number (1-6)")
    first_number = int(sys.stdin.readline())
    if first_number <= 0 or first_number > 6:
        print("Wrong number has been chosen. Select a number from range 1 to 6.")
        two_numbers(round_money, money)
    print("Choose your second number(1-6)")
    second_number = int(sys.stdin.readline())
    if second_number == first_number:
        print("Second number cannot be the same as first number. Try again.")
        two_numbers(round_money, money)
    elif second_number <= 0 or first_number > 6:
        print("Wrong number has been chosen. Select a number from range 1 to 6.")
        two_numbers(round_money, money)
    money_multiplier = 2
    numbers = [first_number, second_number]
    round(numbers, money_multiplier, round_money, money)


def three_numbers(round_money, money):
    print("Choose your first number (1-6)")
    first_number = int(sys.stdin.readline())
    if first_number <= 0 or first_number > 6:
        print("Wrong number has been chosen. Select a number from range 1 to 6.")
        three_numbers(round_money, money)
    print("Choose your second number(1-6)")
    second_number = int(sys.stdin.readline())
    if second_number == first_number:
        print("Second number cannot be the same as first number. Try again.")
        three_numbers(round_money, money)
    elif second_number <= 0 or first_number > 6:
        print("Wrong number has been chosen. Select a number from range 1 to 6.")
        three_numbers(round_money, money)
    print("Choose your third number(1-6)")
    third_number = int(sys.stdin.readline())
    if third_number == first_number:
        print("Third number cannot be the same as first number. Try again.")
        three_numbers(round_money, money)
    elif third_number == second_number:
        print("Third number cannot be the same as first number. Try again.")
    elif second_number <= 0 or first_number > 6:
        print("Wrong number has been chosen. Select a number from range 1 to 6.")
        three_numbers(round_money, money)
    money_multiplier = 3
    numbers = [first_number, second_number, third_number]
    round(numbers, money_multiplier, round_money, money)


def round(numbers, money_multiplier, round_money, money):
    result = random.randint(1, 6)
    print("The result is %s" % result)
    if result in numbers:
        print("Congratulations - you have won!")
        if money_multiplier == 1 and round_money == 1:
            prize = round_money * 2
        else:
            prize = round_money * money_multiplier
        print("Your prize (%s$) has been added to your account." % prize)
        game(money, prize)
    else:
        print("Unfortunately - you have lost.")
        prize = 0
        game(money, prize)


def empty_account():
    print("Your account is empty. Do you want to restart? (1 for yes, 2 for no)")
    restart = int(sys.stdin.readline())
    if restart == 1:
        start()
    elif restart == 2:
        quit()
    else:
        print("Wrong input. Try again")
        empty_account()


start()