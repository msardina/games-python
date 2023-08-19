import random



def ask():
    num = random.randint(1, 100)
    anwser_user = int(input("Num: "))
    tries = 1
    while True:
        if  anwser_user == num:
            print(f"Bingo! You made it in {tries} try(s)")
            print("Lets go again!")
            tries = 1
            anwser_user = int(input("Num: "))
            num = random.randint(0, 100)

        else:
            tries = tries + 1
            if  anwser_user < num:
                print("To small!")
                anwser_user = int(input("Num: "))
            elif anwser_user > num:
                print("too big!")
                anwser_user = int(input("Num: "))
ask()