# John Ressurreicao Pedro Torres
from datetime import datetime
from random import *

# Creates order number
Order_Number = randint(100, 999)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$                 J & Parby's                 $")
print("$          The Best Knock-off Arby's          $")
print("$                                             $")
print("$                  :Chicken:                  $")
print("$                                             $")
print('$      Supreme Chicken Hot Pocket: $5.25      $')
print("$                                             $")
print("$                    Beef:                    $")
print("$                                             $")
print("$      Big Papa's Beef Hot Pocket: $6.25      $")
print("$                                             $")
print("$                    Fish:                    $")
print("$                                             $")
print("$           Shark Hot Pocket: $5.75           $")
print("$                                             $")
print("$                   :Fries:                   $")
print("$                                             $")
print("$  Small: $1.00  Medium: $1.50  Large: $2.00  $")
print("$                                             $")
print("$                                             $")
print("$                 :Beverages:                 $")
print("$                                             $")
print("$  Small: $1.00  Medium: $1.75  Large: $2.25  $")
print("$                                             $")
print("$                                             $")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("/n" * 2)

# Gets the sandwich input from the user and error checks
while True:
    sandwich = input("Which Sandwich would you like [Chicken][Beef][Fish]: ")
    print("")
    sandwich = sandwich.capitalize()
    if sandwich == "Chicken":
        break
    elif sandwich == "Beef":
        break
    elif sandwich == "Fish":
        break
    else:
        # these are the exceptions
        if sandwich.isdigit():
            print("Silly goose, you can't buy a number sandwich. \n")
        else:
            print("Sorry, but that is not a sandwich that we serve. try again. \n")

# Gets the beverage choice from the user
while True:
    choose_d = input("Do you want a beverage [yes][no]: ")
    print("")
    choose_d = choose_d.capitalize()
    if choose_d == "No":
        choose_d = False
        break
    elif choose_d == "Yes":
        choose_d = True
        while True:
            beverage = input("What size would you want you beverage to be [Small][Medium][Large]: ")
            print("")
            beverage = beverage.capitalize()
            if beverage == "Small":
                break
            elif beverage == "Medium":
                break
            elif beverage == "Large":
                break
            # these are the exceptions
            else:
                if beverage.isdigit():
                    print("A number is not a size, try again. \n")
                else:
                    print(beverage + ", I have never seen that beverage size before! \n")
        break
    else:
        print("That is not a yes or a no! \n")

# Gets choice of fries from user
while True:
    choose_f = input("Do you want a side order of fries [yes][no]: ")
    print("")
    choose_f = choose_f.capitalize()
    if choose_f == "No":
        choose_f = False
        break
    elif choose_f == "Yes":
        choose_f = True
        while True:
            fries = input("What size would you want you fries do you want? [Small][Medium][Large]: ")
            print("")
            fries = fries.capitalize()
            if fries == "Small":
                while True:
                    mega_size = input("Would you like to MEGA-SIZE your order of fries for an extra dollar [yes][no]: ")
                    print("")
                    mega_size = mega_size.capitalize()
                    if mega_size == "No":
                        print("That's unfortunate :c \n")
                        break
                    elif mega_size == "Yes":
                        break
                    else:
                        print("That is not a yes or a no! \n")
                break
            elif fries == "Medium":
                break
            elif fries == "Large":
                break
            else:
                # these are the exceptions
                if fries.isdigit():
                    print("A number is not a size, try again. \n")
                else:
                    print("What an obscure fry size, choose something normal. \n")
        break
    else:
        print("That is not a yes or a no! \n")

# gets ketchup choices from user
while True:
    ketchupPacket = input("You you like to add on ketchup packets for only $0.25 a packets? ")
    print("")
    ketchupPacket = ketchupPacket.capitalize()
    if ketchupPacket == "No":
        ketchupPacket = False
        break
    elif ketchupPacket == "Yes":
        ketchupPacket = True
        while True:
            try:
                numOfPackets = int(input("How many ketchup packets would you like to order? "))
                print("")
                if numOfPackets < 0:
                    print("Invalid Input. You cannot order a negative number of packets. \n")
                else:
                    break
            # the exception
            except ValueError:
                print("Invalid Input. Please enter a whole number. \n")
        break
    else:
        print("That is not a yes or a no! \n")

# Calculations

# Prints out the customers choices
if choose_d and choose_f:
    combo_discount = True
    if ketchupPacket:
        print("You have ordered 1 " + sandwich + " Hot Pocket, 1 " + beverage + " beverage")
        print("1 order of " + fries + " fries, and " + str(numOfPackets) + " ketchup packet(s).")
    else:
        print(" You have ordered 1 " + sandwich + " Hot Pocket, 1 " + beverage + " beverage, and")
        print("1 order of " + fries + " fries. That's a lot of junk food.")
else:
    combo_discount = False
    if choose_d:
        if ketchupPacket:
            print("You have ordered 1 " + sandwich + " Hot Pocket, 1 " + beverage + " beverage, and " + str(
                numOfPackets) + " ketchup packet(s).")
        else:
            print("You have ordered 1 " + sandwich + " Hot Pocket and 1 " + beverage + " beverage.")
    elif choose_f:
        if ketchupPacket:
            print("You have ordered 1 " + sandwich + " Hot Pocket, 1 order of " + fries + "fries, and " + str(
                numOfPackets) + " ketchup packet(s).")
        else:
            print("You have ordered 1 " + sandwich + " Hot Pocket and 1 order of " + fries + "fries.")

print("\n")

# Makes sure the customers' payment is valid
while True:
    try:
        payment = float(input("How much will you be paying us today: "))
        print("")
        payment = payment / 1
        break
    except:
        print("That is not a valid amount!")
        print("")
# calculates sandwich cost
if sandwich == "Chicken":
    s_price = 5.25
elif sandwich == "Beef":
    s_price = 6.25
elif sandwich == "Fish":
    s_price = 5.75
# Receipt

print("                                             ")
print("                 J & Parby's                 ")
print("          The Best Knock-off Arby's          ")
print("             123 Really Cold St.")
print("             Compton, Antarctica")
print("                                             ")
print("                 Order #" + str(Order_Number))
print("          " + str(datetime.now()))
print("                                             ")
print("          " + sandwich + " Hot Pocket:        $" + str(s_price))
print("                                             ")

# calculates beverage cost
if choose_d:
    if beverage == "Small":
        d_price = 1.00
    elif beverage == "Medium":
        d_price = 1.75
    elif beverage == "Large":
        d_price = 2.00

    print("          " + beverage + " Beverage:         $" + str(d_price))
    print("                                             ")
else:
    d_price = 0.00

# calculates fries cost
f_price = 0
if choose_f:
    if fries == "Small":
        f_price = 1.00
    elif fries == "Medium":
        f_price = 1.50
    elif fries == "Large" or mega_size == "Yes":
        f_price = 2.00
    print("          " + fries + " Fries:            $" + str(f_price))
    print("                                             ")
else:
    f_price = 0.00

# calculates ketchup cost
if ketchupPacket:
    k_price = numOfPackets * 0.25
    print("          " + str(numOfPackets) + " Ketchup Packets:      $" + str(k_price))
    print("                                             ")
else:
    k_price = 0.00

# calculates combo discount
if combo_discount:
    total = (s_price + d_price + f_price + k_price) - 1.00
    print("          Combo Discount          -$1.00")
    print("                                             ")
    print("          Total:                  $" + str(total))
else:
    total = (s_price + d_price + f_price + k_price)
    print("          Total:                  $" + str(total))

# calculates change
change = payment - total
print("          Amount Paid:            $" + str(payment))
print("          Change:                 $" + str(change))
print("                Have a good day :D")

input('Press ENTER to exit')
