from random import randint
from art import logo
print(logo)

easy_level = 10
hard_level = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high") 
        return turns - 1
    elif guess < answer: 
        print("Too low")
        return turns - 1
    else:
        print(f"You got it.  The answer is {answer}.")
        turns -= 1
    
def set_difficulty():
    level = input("Chosse a difficulty.  Type 'easy' or 'hard'. ")
    if level == "easy":
        return easy_level
    else:
        return hard_level

def game():
    print("Welcome to the guessing game.")
    print("I have chosen a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Actual answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} guesses remaining.")
        
        guess = int(input("Guess the number: "))
        
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You ran out of guesses, you lose.")
            return    
        elif guess != answer:
            print("Guess again")
game()        



