"""
Title: Number Riddler

Author: Makayla Wray

Date: 2023-10-17

Description: This program allows the user to play a number guessing game.
"""

import random


def main():
    welcome()
    play_game()


def welcome():
    
    """This function creates a welcome message for the player"""
    
    print("Welcome to the Guess the Number game.")
    print()
    print("I have selected a number between 1 and 100.")
    print("Your goal is to guess it in as few guesses as possible.")
    print("You may type -999 when you want to stop the game at anytime.")
    print()
    print("Let’s get started.")
    print()
    
def play_game():
    
    """This fuction will ask the player for a number until it matches
    the computer's picked number and display the current range to guess between """
    
    comp_num = random.randint(1,100) 
    game = True
    
    attempts = 1 
    user_range_min = 1  
    user_range_max = 100 
    
    while game:
        
        guessed_num = int(input(f"Guess a number between {user_range_min} and {user_range_max}: "))
        print()
        
        if guessed_num == comp_num:
            print(f"Congratulations you guessed the number after {attempts} guesses!")
            print()
            game = False
            play_again = str(input("Do you want to play again (y or n)?"))
            
            while play_again != "y" and play_again !="n":
                print()
                print("I’m sorry, I do not understand that answer.")
                print()
                play_again = input("Do you want to play again (y or n)?")
                print()

            if play_again == "y":
                print("Great! Let’s play again.")
                print()
                play_game()

            else:
                game = False
                print("Okay. Thanks for playing!")
                
        elif guessed_num > comp_num: 
            if guessed_num > user_range_max:
                print("Invalid guess. The number is out of range. Your guess doesn't count. Please guess again")
                print()

            else:
                user_range_max = guessed_num - 1 
                print("Incorrect guess. Your guess is too high. Please guess again.") 
                print()
            
        elif guessed_num == -999:
            print()
            print("You have quit the game. Thanks for playing!")
            break
        
        elif guessed_num < comp_num: 
            if guessed_num < user_range_min:
                print("Invalid guess. The number is out of range. Your guess doesn't count.Please guess again")
                print()

            else:
                user_range_min = guessed_num +1 
                print("Incorrect guess.  Your guess is too low. Please guess again.")
                print()
      
        attempts +=1

main()

#Thank you for playing the game! Have fun.
