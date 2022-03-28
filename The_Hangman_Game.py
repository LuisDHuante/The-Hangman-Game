import random
import os
import re

regex = re.compile('[@_!#$%^¿&*()<>?/\|}{~:]')


def hangman_drawings(number):
    if number == 10:
        print('''
 +----+
 |    |
      |
      |
      |
      |
=========''')
    if number == 9:
        print('''
 +----+
 |    |
      |
      |
      |
      |
=========''')
    if number == 8:
        print('''
 +----+
 |    |
      |
      |
      |
      |
=========''')
    elif number == 7:
        print('''
 +----+
 |    |
 O    |
      |
      |
      |
=========''')
    elif number == 6:
        print('''
 +----+
 |    |
 O    |
 |    |
      |
      |
=========''')
    elif number == 5:
        print('''
 +----+
 |    |
 O    |
/|    |
      |
      |
=========''')
    elif number == 4:
        print('''
 +----+
 |    |
 O    |
/|\   |
      |
      |
=========''')
    elif number == 3:
        print('''
 +----+
 |    |
 O    |
/|\   |
/     |
      |
=========''')
    elif number == 2:
        print('''
 +----+
 |    |
 O    |
/|\   |
/ \   |
      |
=========''')
    elif number == 1:
        print('''
 +----+
 |    |
 |    |
 O    |
/|\   |
/ \   |
=========''')


def add_word():
    new_word = input('Add the new word: ').lower()
    while True:
        if new_word.isalpha():
            os.system ("clear")
            break
        elif new_word.isalnum() or regex.search(new_word) != None:
            os.system ("clear")
            new_word = input('You must enter a valid word : ').lower()
    with open('./archivos/data.txt', 'a', encoding='utf-8') as file:  
        file.write('\n')
        file.write(new_word)
        

def game_menu():
    while True:
        try:
            os.system ("clear")
            the_hangman_message()
            option = int(input("""
1. Safe mode
2. Danger mode 
3. Instructions
4. Return to Main Menu\n
Select an option: """))
            if option == 1:
                os.system ("clear")
                gamemode1()
                os.system ("clear")
            elif option == 2:
                os.system ("clear")
                gamemode2()
                os.system ("clear")
            elif option == 3:
                os.system ("clear")
                print("""
    1. In Safe mode, you have infinite lives, which means you can try any number of letters to win the game.\n
    2. In Danger mode, you have a limited amount of attempts (lives) to guess the word and save the hangman. \n""")
                input('Press any key to return to game menu')
                os.system ("clear")
            elif option == 4:
                break
        except ValueError:
            os.system ("clear")
            print('Choose a valid option\n')
            input('Press any key to return to game menu')
            os.system ("clear")


def main_menu(list):
    while True:
        try:
            os.system ("clear")
            the_hangman_message()
            option = int(input("""Welcome to The Hangman!\n
1. Start game
2. Add word to the game
3. Credits
4. Quit

Select an option: """))
            if option == 1:
                os.system ("clear")
                game_menu()
                os.system ("clear")
            elif option == 2:
                os.system ("clear")
                add_word()
                print('The word has been added!\n')
                input('Press any key to return to main menu')
                os.system ("clear")
            elif option == 3:
                os.system ("clear")
                credits()
                input('Press any key to return to main menu')
                os.system ("clear")
            elif option == 4:
                os.system ("clear")
                break
        except ValueError:
            os.system ("clear")
            print('Choose a valid option\n')
            input('Press any key to return to main menu')
            os.system ("clear")


def no_danger_man():
    print("""      
    __________
     |/     
     |       _  HAHAHA
     |      (_)
     |      \|/
     |       |
     |	     |
 ____|___   / \ \n""")
    

def credits():
    print("""
    

_  _ ____ ___  ____    ___  _   _    _    _  _ _ ____    ___  ____ _  _ _ ___     _  _ _  _ ____ _  _ ___ ____ 
|\/| |__| |  \ |___    |__]  \_/     |    |  | | [__     |  \ |__| |  | | |  \    |__| |  | |__| |\ |  |  |___ 
|  | |  | |__/ |___    |__]   |      |___ |__| | ___]    |__/ |  |  \/  | |__/    |  | |__| |  | | \|  |  |___ 
                                                                                                               

 """)
    


def defeat_message():
    print("""

     __                __   __  ___ 
\ / /  \ |  |    |    /  \ /__`  |  
 |  \__/ \__/    |___ \__/ .__/  |  \n
""")
 

def victory_message():
    print("""                                        
 _   _  ___  _   _  __      _____  _ __  
| | | |/ _ \| | | | \ \ /\ / / _ \| '_ \ 
| |_| | (_) | |_| |  \ V  V / (_) | | | |
 \__, |\___/ \__,_|   \_/\_/ \___/|_| |_|
  __/ |                                  
 |___/        \n""")



def the_hangman_message():
    print(""" 

 _   _              _                                             
| | | |            | |                                            
| |_| |__   ___    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| __| '_ \ / _ \   | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |_| | | |  __/   | | | | (_| | | | | (_| | | | | | | (_| | | | |
 \__|_| |_|\___|   |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                       __/ |                      
                                      |___/                       """)



def replacements(word):
    #El método maketrans crean una tabla de mapeo
    #y el método translate() reemplaza cualquier 
    # carácter "S" con un carácter "P".
    new_sentence = word.maketrans('ÁÉÍÓÚ', 'AEIOU')
    return word.translate(new_sentence)


def chosen_word():
    word = random.choice(list_from_archive())
    return word.upper()


def list_from_archive():
    with open('./archivos/data.txt','r',encoding='utf-8') as f:    
        word_list = [word.replace('\n','') for word in f]
    return word_list


def gamemode1(points=0):
    word = list(replacements(chosen_word()))
    word_to_verify = ['-' for c in word]
    list_of_letters = []


    while True:
        while word != word_to_verify: 
            no_danger_man()
            print('Guess the word! \n',*word_to_verify)
            letter_input = input('\nInsert a letter: ').upper()
            os.system ("clear")
            letter_input_flag = True
            os.system ("clear")
            if letter_input_flag != letter_input.isalpha():
                os.system('clear')
                print('You must enter a valid character ')
                print('You have entered the following letters: ', *list_of_letters)
            if letter_input in list_of_letters:
                os.system('clear')
                print('You already entered that letter ')
                print('You have entered the following letters: ', *list_of_letters)
            if letter_input not in list_of_letters  and len(letter_input)==1 and letter_input.isalpha():
                list_of_letters.append(letter_input)
            else: 
                continue
            os.system('clear')
            print('You have entered the following letters: ', *list_of_letters)
                
            #Usamos la función enumerate para acceder a los índices 
            # word.index(letra) siempre devolverá el primer índice de letter en word.
            for index,letter in enumerate(word):
                if letter_input == letter :
                    word_to_verify[index] = letter
            else:
                continue


        if word == word_to_verify:
            os.system ("clear")
            victory_message()
            print('The word was', *word)
            points += 1
            if points == 1:
                print('You have ' + str(points) + ' point.\n')
            else:
                print('You have ' + str(points) + ' points.\n')
            print('Do you want to play again?')
            option = input('Press Y to continue or any key to exit to main menu: ').upper()
            if option == 'Y':
                os.system ("clear")
                gamemode1(points)
                break
            else:
                os.system ("clear")
                break

def gamemode2(points=0):
    word = list(replacements(chosen_word()))
    word_to_verify = ['-' for c in word]
    lives = 10
    list_of_letters = []

    while True:
        os.system ("clear")
        while word != word_to_verify: 
            hangman_drawings(lives)
            print('Guess the word! \n',*word_to_verify)
            print('Lives: '+ str(lives))
            letter_input = input('\nInsert a letter: ').upper()
            letter_input_flag = True
            os.system ("clear")
            if letter_input_flag != letter_input.isalpha():
                os.system('clear')
                print('You must enter a valid character ')
                print('You have entered the following letters: ', *list_of_letters)
            if letter_input in list_of_letters:
                os.system('clear')
                print('You already entered that letter ')
                print('You have entered the following letters: ', *list_of_letters)
            if letter_input not in list_of_letters  and len(letter_input)==1 and letter_input.isalpha():
                list_of_letters.append(letter_input)
            else: 
                continue
            os.system('clear')
            print('You have entered the following letters: ', *list_of_letters)
           

            #Usamos la función enumerate para acceder a los índices 
            # word.index(letra) siempre devolverá el primer índice de letter en word.
            for index,letter in enumerate(word):
                if letter_input == letter :
                    word_to_verify[index] = letter
            if letter_input not in word:
                lives -=1
            else:
                lives = lives
            if lives == 0:
                defeat_message()
                print('The word was', *word,'\n')
                input('Press any key to return to main menu')
                os.system ("clear")
                break


        if word == word_to_verify:
            os.system('clear')
            victory_message()
            print('The word was', *word)
            points += 1
            if points == 1:
                print('You have ' + str(points) + ' point.\n')
            else:
                print('You have ' + str(points) + ' points.\n')
            print('Do you want to play again?')
            option = input('Press Y to continue or any key to exit to main menu: ').upper()
            if option == 'Y':
                os.system ("clear")
                gamemode2(points)
                break
            else:
                os.system ("clear")
                break
        break


def play_hangman():
    main_menu(list_from_archive())
   

def run():
    play_hangman()


if __name__ == '__main__':
    run()
