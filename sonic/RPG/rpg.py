import cmd
import textwrap
import sys
import time
import os
import random

screen_width = 100

# Player setup
class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        
my_player = player()

# title screen
def title_screen_selections():
    option = input("> ")
    if option.lower == ('play'):
        #start_game()
        pass
    elif option.lower == ('help'):
        #help_menu()
        pass
    elif option.lower == ('quit'):
        sys.exit()
    while option.lower not in ['play', 'help', 'quit']:
        print('!@#$%*()Error!@#$%*()')
        print("*********Possible reasons*********")
        print('         Non valid command        ')
        option = input("> ")
        if option.lower == ('play'):
            #start_game()
            pass
        elif option.lower == ('help'):
            #help_menu()
            pass
        elif option.lower == ('quit'):
            sys.exit()
            
def title_screen():
    os.system('clear')
    print('################################')
    print('#   Welcome to this text RPG   #')
    print('################################')
    print('#         --Options --         #')
    print('#######                  #######')
    print("#         -- Play --           #")
    print("#         -- Help --           #")
    print("#         -- Quit --           #")
    print("#Copyright Marcos Sardina 2022 #")
    print("################################")
    title_screen_selections()
    
def help_menu():
    print('###################################')
    print('#      This is the help menu      #')
    print('###################################')
    print('#Use Up, Down, Left, Right to move#')
    print('#######                  ##########')
    print("#     Type 'look' to inspect      #")
    print("#  Type these command to do them  #")
    print("#                                 #")
    print("#  Copyright Marcos Sardina 2022  #")
    print("###################################")
    title_screen_selections()
    
def start_game():
    print("Game on!!!")
    