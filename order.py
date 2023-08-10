# import from pizzaReceipt
from pizzaReceipt import *

# PIZZA_SIZE tuple provides sizes of pizzas
PIZZA_SIZE = ('S','M', 'L', 'XL')
# intialize pizzaOrder as a empty list
pizzaOrder= []

#constant TOPPINGS containing 15 toppings available for pizza
TOPPINGS = ('ONION', 'TOMATO', 'GREEN PEPPER', 'MUSHROOM', 'OLIVE', 'SPINACH', 'BROCCOLI', 'PINEAPPLE', 'HOT PEPPER', 'PEPPERONI', 'HAM', 'BACON', 'GROUND BEEF', 'CHICKEN', 'SAUSAGE')

#while prompting user if they would like to order pizza; If they enter Q or NO or a space then break out of the loop
#otherwise, ask for size of pizza
orderInput = ""
#stop running if user entered Q or NO
orderInput = input("Do you want to order a pizza: ")
while True:
    if orderInput.upper() == 'Q' or orderInput.upper() == 'NO' or orderInput.upper() == '':
        break

    else:
        sizeInput = ""
        #while the size is not in the PIZZA_SIZE tuple, then keep prompting user to enter size until they do not enetr size in tuple
        while sizeInput.upper() not in PIZZA_SIZE:
            sizeInput = input("Choose a size: S, M, L, or XL: ")
            #if size user inputed is not in tuple then execute next part of iteration , and if it is in the tuple then break out of loop
            if sizeInput.upper() not in PIZZA_SIZE:
                continue
            elif sizeInput.upper() in PIZZA_SIZE:
                break

        # list that will hold the whole order of toppings
        toppingInput = ""
        topping = []

        #while user didnt input X, ask to enter topping in LIST and provide LIST if they prompt to print to TOPPINGS tuple to screen
        #if topping suer prompted are in tuple of TOPPINGS then print that the topping they prompted has been add to their pizza and add the topping to the topping list
        #otherwise is the topping user prompted is not in the tuple of TOPPINGS or list or his not X then tell user that they have entered invalid topping
        while toppingInput.upper() != 'X':
            toppingInput = input('Type in one of our toppings to add it to your pizza. To see the list of toppings, enter "LIST". When you are done adding toppings, enter "X"\n')
            if toppingInput.upper() == 'LIST':
                print(TOPPINGS)
            if toppingInput.upper() in TOPPINGS:
                print(f'Added {toppingInput.upper()} to your pizza')
                topping.append(toppingInput.upper())
            elif toppingInput.upper() not in TOPPINGS or toppingInput.upper() not in "LIST" or toppingInput.upper() not in "X":
                print("Invalid topping")

        #add the size of the pizza and the toppings in the pizzaOrder list and prompt user if they want more pizza
        #if they enter Q or No, then break out of the loop otherwise execuet next iteration
        pizzaOrder.append((sizeInput.upper(), topping))
        morePizza = input('Do you want to continue ordering: ')
        if morePizza.upper() == 'Q' or morePizza.upper() == 'NO':
            break
        else:
            continue

#call generatReciept method
generateReceipt(pizzaOrder)

