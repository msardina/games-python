def menu():

    options = ["Book reservation", "Check reservation", "Cancel recervation", "Change recervation", "Quit"]
    for i in range(1, len(options)+ 1):
        print(f"{i}. {options[i-1]}")
    

    choose_option = input("Which one do you want to do?(put number) ")
    if choose_option == "1":
        print("You've booked")
    if choose_option == "2":
        print("Today")
    if choose_option == "3":
        print("You've Canceled your recervation.")
    if choose_option == "4":
        date = input("When do you want it?(put date slash way) ")
        print(f"Your recervation is at {date}")

menu()