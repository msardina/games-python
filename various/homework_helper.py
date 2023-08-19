import time
import random

def make_space(space): # make terminal space(Blank lines)
    for i in range(1, space):
        print()

make_space(3)

# start 
words = []
word = "hello"
while not word == "":
    word = input("Word: ")
    
    if word == "":
        continue    
    
    if word in words:
        print("sorry but that word already exists!")
    else:
        print("Word added!")
        words.append(word)
    
    
    list = input("Do you want me to show you all the words you have?  (y/n/m) ")
    
    if list == "y":   
        print(words)
    if list == "m":
        for i in range(0, 25):
            print("Randomizing!!!!!")
            time.sleep(0.10)
            
        randomy = random.randint(0, 1)
        
        if randomy == 0:
            print(words)

            
print(f"You have {len(words)} words")
print(words)