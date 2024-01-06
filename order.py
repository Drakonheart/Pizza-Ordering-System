TOPPINGS = ("ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE", "SPINACH","BROCCOLI", "PINEAPPLE", "HOT PEPPER", "PEPPERONI", "HAM", "BACON", "GROUND BEEF", "CHICKEN", "SAUSAGE")
sizes = ["S", "M", "L", "XL"] # These will be twh 4 types of toppings that we will be serving
pizzaOrder = []         # This list will be storing the pizza order with their infomration ('size',  [toppings]) in a tuple.
wantPizza = input("Do you want to order a Pizza? ")
OrderComplete = False
while OrderComplete == False:       # This loop will run as long as the user wants to order more pizza indicated by the OrderComplet == False.
    if wantPizza.upper() == "NO" or wantPizza.upper() == "Q":       # This condition is made if the user does not wish to continue ordering pizza (hence cancelling the order).
        print("You did not order anything.")
        exit()
    else:
        sizeConfirmation = False
        while sizeConfirmation is False:        # This loop will determine the size of the pizza and will continue to ask for the size pizza until the user inputs the appropriate size!
            sizePizza = input("Choose a size: S, M, L, or XL: ")        # Note the size must be the abbreviation example: [S, M, L, Xl).
            if sizePizza.upper() in sizes:          # If the user inputs the correct size then the loop will end and will be stored in the variable sizePizza
                sizeConfirmation = True
        storeToppings = []      # This list will store the toppings picked by the user.
        toppingConfirmation = False
        while toppingConfirmation is False:         # This loop is used to ask a number of questions depending on the user and the number of toppings they wish to order!
            askToppings = input('''Type in one of our toppings to add it to your pizza. To see the list of toppings, enter "LIST". When you are done adding the toppings enter \"X\"''' + "\n")
            if askToppings.upper() == "LIST":       # This will print the 'list' of toppings that we currently offer.
                print(TOPPINGS)
            elif askToppings.upper() in TOPPINGS:       # This will check if the topping(s) that the user has picked is a valid.
                print(f"Added {askToppings.upper()} to your pizza  ")
                storeToppings.append(askToppings.upper())       # Will add to the list of storeToppingOrder.
                toppingConfirmation = False         # And will continue asking the same question...
            elif askToppings.upper() == "X":        # Until they input "X".
                toppingConfirmation = True      # The number of questions regarding the topping will come to an end!
            else:
                print("Invalid topping")        # Else if the topping is invalid it will state it and will keep asking the askTopping question until they input "X"!
        tempPizza = (sizePizza.upper(), storeToppings)      # Here it will be storing the above information in a tuple including the size of the pizza and the list of toppings!
        pizzaOrder.append(tempPizza)        # And will be added to the pizzaOrder list that will be used to generate our final receipt.
    morePizza = input("\nDo you want to continue ordering? ")       # Here we will ask if the user wants to order additional pizza(s)...
    if morePizza.upper() == "NO" or morePizza.upper() == "Q":       # If "NO" or "Q"  the original loop or known as the orderConfirmation will end!
        OrderComplete = True
    else:
        OrderComplete = False       # Else the program will run again to store the required information for pizza 2, 3, 4... and so on
from pizzaReceipt import generateReceipt
generateReceipt(pizzaOrder)
        #  Here we will be importing our pizzaReceipt file and calling the generateReceipt which will take pizzaOrder as its argument or parameter to generate the user's order receipt.
