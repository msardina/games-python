import random
import time
import sys



def game_on():
        print('Game on')
        time.sleep(1)
        for i in range(0, 10):
                print("################")
                time.sleep(0.10)
        for j in range(0, 10):
                print()
                time.sleep(0.10)
                
        name = input('Hi! What is your name? ')
        print(f'{name}? That a nice name.')
        print('Nice to meet you!')
        feeling = input("How are you feeling? ")
        print("Sorry but like everyone Im getting older and deafer! I couldnt hear you. Hope its good though!")
        time.sleep(3)
        print("Hey Ive got an Idea!")
        time.sleep(2)
        print("Lets play a game!")
        time.sleep(2)
        print("Of Hide and seek!")
        time.sleep(2)
        print("But before we start...")
        time.sleep(2)
        print("let me tell you a secret.")
        time.sleep(2)
        print("I")
        time.sleep(2)
        print("AM")
        time.sleep(2)
        print("EVIL!")
        time.sleep(0.10)
        print("HAHAHHAHAHAHHAHAHAHHAHAHA")
        time.sleep(1)
        print("I DO NOT WANT TO PLAY HIDE AND SEEK!")
        time.sleep(2)
        print("I WANT TO PUT YOU IN MY SECRET EVIL PRISN!")
        time.sleep(2)
        time.sleep(2)
        print("(Evil Pearson Locks You Up In Their Secret Prisn)")
        time.sleep(2)
        print("NOW I MAY CONTINUE MY PLAN TO TAKE OVER THE WORLD!")
        time.sleep(2)
        print("In 10 minutes the world will be mine!")
        time.sleep(2)
        print("HAHAHHAHAHAHA")
        timer = 600
        print(f'{timer} seconds left until destruction')
        for i in range(0, 10):
                print('##########')
        print("Level 1: Escaping the prisn")
        print("DUDUDUDUDUUDUDUUDDUUUUDUUUDUUUDUDUDUDUDUDUDUUD")
        action = input("> ")
        while not action == 'inspect':
                print("You have no Idea where you are. Maybe you should inspect the room before doing anything else.")
                action = input("> ")
        print("The jail has stoned walls as thick as a rhino.")
        print("There are no windows or doors.")
        print("No food, No Items, No way of escape.")
        action = input("> ")
        if action == 'look in your pockets':
                print("You look in your pockets and feel something big. You bring it out and find a rocket launcher. You have no Idea why theres a rocket launcher in your tiny pockey but you dont care. You also find a gigantic peace of metal and put it on your head. You fire You fire the rocket launcher and lift off the ground. You Crash throught the walls of the Prisn. The metal peace is protecting you head. Wich is good.You break through the last wall of the prisn and now you have escaped the prisn. ")
                print("Level 2: The fall")
                continuea = input("Continue: ")
                print("Your at the top of the prisn(12020303004050350500 feet up).You cant go up beacuase the rocket launcher has lost its power. You cant go down cause you die beacause of the height.")
                action = input("> ")
                if action == "inspect":
                        print("Its a sunny day. Theres a box(You dont know whats inside.).")
                        print("Theres also a parachute. Aswell as a bunch of plungers.")
                        action = input("> ")
                        if action == 'look inside the box':
                            print("You open the box and see a grenade. You activate it by accident and you explode. You die. The world Dies. The end")
                            sys.exit()
                        elif action == "use parachute":
                            print("You grab the parachute. Put on your back and jump off the roof.")
                            print("Turns out the parachute was not a parachute but a normal bag. Your falling at super speeds.")
                            print("When you think your gonna die, superman comes flying and saves you!!! Your saved! Sort of. :/ It wasnt superman")
                            print("It was superbad the supervillian! He kills you. You Die. The world Dies. THE END!")
                            sys.exit()
                        elif action == "use plungers":
                            print("You grab the Plungers and stick it to the side of the prisn. You put your hands on the plungers.")
                            print("Your now sticking to the side of the prisn.You climb down using the plungers and get to the bottom of the prisn.")
                            print("Youve escaped the fall.")
                            print("Level 3: The Secret Lab")
                            countinuea = input("Continue: ")
                            print("You start walking randomly to see if you can find anything.")
                            print("Suddenly you fall through a hole in the ground and find yourself in a crazy lab.")
                            print("You see a sign that says 'Mr.Poopi Pants Secret Lab(AKA evil pearson)'")
                            print("One step closer to saving earth. Its his lab. The evil mans lab.")
                            print("You see a door saying DO NOT DISTURB")
                            print("Awell as another one that says  'loot in here' ")
                            action = input("To use a door write use + door name + door > ")
                            if action == 'use loot in here door':
                                print("You open the door and see piles and piles of money. Everywhere you looked there was money. You decide to swim in it.")
                                print("You get distracted and the minutes fall down 1 by 1. Suddenly after 5 minutes you hear explosions. The world dies. The end.")
                                sys.exit()
                            elif action == "use DO NOT DISTURB door":
                                print("You enter the room and see a big machine.")
                                print("On it, it said 'Destroy world machine'")
                                print("This is the thingy that the evil man will use to destroy earth!")
                                action = input("> ")
                                if action == 'inspect':
                                    print("The machine has a lever marked quit destruction")
                                    action = input("To pull the lever type 'pull lever'> ")
                                    if action == 'pull lever':
                                        print("You pull the lever and the destruction is canceled.The machine explodes and you have saved earth. The police arrests Mr.Poopi Pants and you live happily ever after!")
                                    else:
                                        print(f"Your about to {action} when suddenly Mr.Poopi Pants comes in.")
                                        print(f"He says   'We Meet again Lord {name} of the stupids'")
                                        print("You fight for a minute until the machine explodes and the world dies. The end")
                                        sys.exit()
                            else:
                                if not action == 'use loot in here door' or not action == 'use DO NOT DISTURB door':
                                    print(f"You cant {action} so you just stay where you are. Then after 2 minutes , The world dies. The end")
                                    sys.exit()
                else:
                        if not action == 'look inside the box' or not action == 'use parachute' or not action == 'use plungers':
                            print(f"Youre about to {action} when suddenly you trip on a rock.")
                            print("You twist your ankel and cant move for 10 minutes. The ten minutes pass and the world dies. THE END")
                            sys.exit()
                
        elif action.lower == "run into a wall":
                print("You run into a wall and go unconsius. The ten minutes pass by and the world is dead. The end.")
                sys.exit()
        else:
                if not action == 'look in your pockets' or not action == 'run into a wall':
                        print("Just as your about to do that. The evil man comes and zaps you.You forget everything. Even who you are. What youre doing. Where you are. Whats 1 + 1. And sadly what you were going to do. The ten minutes pass by and the world dies.  The end.")
                        sys.exit()
                
        
        
####### Title Screen #######
def title_screen():
        for j in range(0, 100):
                print()
        print('##################################')
        print('#        WORLD DESTRUCTION       #')
        print('##################################')
        print('#       Write play to play       #')
        print('#                                #')
        print('#                                #')
        print('# Copyright Marcos Sardina 2022  #')
        print('##################################')
        print()
        play = input("> ")
        if play == 'play':
                game_on()
      
######## game code ########   
load_time = random.randint(20, 40)
for i in range(0, load_time):
    print('Loading... Please wait...')
    time.sleep(0.10)
        
print("Finished!")
time.sleep(5)
title_screen()

