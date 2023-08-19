keep_going = 2
house_money = 1400
print(f"The house is ${house_money}")
money = 2000
payed_money = 0
print(f"you have ${money} to waste!")

for day in range(1, 8):
    if not keep_going == 0:
        pay_money = ""
        print(f"Day {day}")
        pay_money = int(input("Pay your money here: "))
        if money > 0:
            money =  money - pay_money
            payed_money = payed_money + pay_money
            print(f"Your money: ${money}")
            print(f"payed money: ${payed_money}")
            keep_going = 1
        if money < 0:
            print(f"Sorry you  can not pay the house: you have less than 0$ of money. here is your ${payed_money}")
            keep_going = 0



if payed_money > house_money and not keep_going == 0:
    print("You win the house!")
if payed_money == house_money and not keep_going == 0:
    print(f"You paid ${payed_money} and the house was ${house_money}!! You win the house! doodoodoobadoo!!")
elif payed_money <= house_money and not keep_going == 0:
    print(f"Sorry no house for you. You payed ${payed_money} and the house was ${house_money}")