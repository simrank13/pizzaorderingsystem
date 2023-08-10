#created a function that prints out receipt of the entire order sent through pizzaOrder
#make toppingCost, baseCost and tax global variables to read and write global variable insdie generateReciept function
def generateReceipt(pizzaOrder):
    global toppingCost, baseCost, tax
    #if pizzaOrder is empty then tell user that they didnt order anything otherwise print the order by starting to print your order to the screen
    if len(pizzaOrder) == 0:
        print("You did not order anything")
        return

    # define and initialize totalCost as a sentinel value so that it allows different number of inputs by the user each time
    # define and initialize pizzaCount as 0
    totalCost = 0.0
    pizzaCount = 0

    print('Your order: ')
    #for each element in the pizzaOrder list, declare the size to be the first element in list, the toppings will be the second element of the list
    #the number of pizzas will increment by 1 and size of the pizza will be processed as in capital form regardless of inputted in lower case or capitals
    for pizza in pizzaOrder:
        pizzaSize = pizza[0]
        pizzaCount += 1
        pizzaToppings = pizza[1]
        pizzaSize = pizzaSize.upper()

        #if pizzaSize is following size: S,M,L or XL, then provides the baseCost and toppingCost of following size while updating to total cost variable making it be the baseCost of pizza
        if pizzaSize == 'S':
            baseCost = 7.99
            toppingCost = 0.50
        elif pizzaSize == 'M':
            baseCost = 9.99
            toppingCost = 0.75
        elif pizzaSize == 'L':
            baseCost = 11.99
            toppingCost = 1.00
        elif pizzaSize == 'XL':
            baseCost = 13.99
            toppingCost = 1.25
        #updating totalCost variable
        totalCost += baseCost

        #print number of pizza, with size and format baseCost variable to 2 decimals
        #for every topping the user enters that is in pizzaToppings print the toppings and append it into pizzaToppings empty list
        print(f'Pizza {pizzaCount}: {pizzaSize}  %11.2f' % (baseCost))
        for topping in pizzaToppings:
            print(f'-{topping}')

        #initialize addCost variable to be 0
        #if user enters more than 3 toppings then add the additonal cost of the toppings to baseCost updating private cost
        addCost = 0
        if len(pizzaToppings) > 3:
            addCost = (len(pizzaToppings) - 3) * toppingCost
            # updating totalCost variable
            totalCost += addCost
            #the number of toppings is initialized as the length of the pizzaToppings variable
            #while the number of toppings are greater than 3, print the size of the pizza and format the toppingCost to 2 decimals and decrement toppingNum by 1 each time
            toppingNum = len(pizzaToppings)
            while toppingNum > 3:
                print(f'Extra Topping ({pizzaSize})  %3.2f' % (toppingCost))
                toppingNum -= 1
    #declare and initialize tax rate as 13% and multiple it with the total cost to get the tax amount and add the tax amount to the total cost to update the total cost
    TAX_RATE = 0.13
    tax = totalCost * TAX_RATE
    # updating totalCost variable
    totalCost += tax
    #print the tax and total while formating both the tax and the total cost to 2 decimals
    print(f'Tax: %18.2f' % (tax))
    print(f'Total: %16.2f' % (totalCost))
    return