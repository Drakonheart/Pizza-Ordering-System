TAXRATE = 0.13 # Ontario sales tax is a value that stays the same throughout our program.
allCostOfPizza = [] # This list will store the cost of pizza for later use.
allCostOfToppings = [] # This list will store the cost of toppings for later use.
def generateReceipt(pizzaOrder): # This function will take the number of pizzaOrder from the user.
    if pizzaOrder == []: # If the pizzaOrder is an empty list then it will indicate to the user that they have ordered nothing.
        print("You did not order anything")
    else:
        numberOfPiz = []
        for numberOfPizza in range(0, len(pizzaOrder)): # This loop will determine the number of pizzas that the user has created based on the length of pizzaOrder.
            numberOfPizza = numberOfPizza + 1
            numberOfPiz.append(numberOfPizza) # Will store the number pizza for later use.
        print("Your order:")
        for p in pizzaOrder:        # p will denote the elements in the the pizzaOrder
            if p[0] == "S":         # p[0] indicates if each pizza tuple at index 0 matches the appropriate size picked by the user (S pizza) and if so it will execute the bellow program!
                pizzaCostS = 7.99
                allCostOfPizza.append(pizzaCostS)       # Adding the cost of Small pizza to the list.
                print(f"Pizza {numberOfPiz[0]}: " + p[0] + "                 " + str(pizzaCostS))       # Printing the pizza size and cost indicated with the pizza number.
                numberOfPiz.pop(0)       # This line will simply delete the number associated with each pizza and use the next appropriate number for the next pizza.
                for chosenTopps in p[1]:        # This for loops will simply check the chosen toppings (in S pizza) in the pizzaOrder list at index 1 (the list of toppings).
                    print(f"- {chosenTopps}")
                if len(p[1]) > 3:       # This condition is used to compare and see if the user has picked more than three toppings on their pizza.
                    topKeep = (len(p[1]) - 3) * 0.50        # If so it will calculate the total cost of the addition cost of toppings after the three chosen toppings!
                    addCostS = format(0.5, '.2f')
                    allCostOfToppings.append(topKeep)       # Adding the cost of toppings to the list
                    for x in range(0, len(p[1]) - 3):       # This loop will determine the number times the additional topping cost and description will be printed out.
                        print((f"Extra Topping ({p[0]})" + "          " + f"{addCostS}"))
            # NOTE there rest of the program will be similar thus I will keep the comments a bit shorter <3!
            if p[0] == "M":         #p[0] indicates if each pizza tuple at index 0 matches for (M) Pizza
                pizzaCostM = 9.99
                allCostOfPizza.append(pizzaCostM)       # Appending the costM.
                print(f"Pizza {numberOfPiz[0]}: " + p[0] + "                 " + str(pizzaCostM))
                numberOfPiz.pop(0)      # This line will delete the number associated with each pizza and use the next appropriate number.
                for chosenTopps in p[1]:         # This for loop checks the chosen toppings in pizzaOrder for (M pizza).
                    print(f"- {chosenTopps}")
                if len(p[1]) > 3:       # This condition checks if the user has picked more than three toppings on their M pizza.
                    topKeep = (len(p[1]) - 3) * 0.75 # If so it will calculate the total cost of the additional cost of toppings after the three chosen toppings!
                    addCostM = 0.75
                    allCostOfToppings.append(topKeep)       # Appending the cost of toppings to the list
                    for x in range(0, len(p[1]) - 3):       # The additional toppings will be printed out!
                        print(f"Extra Topping ({p[0]})" + "          " + str(addCostM))
            if p[0] == "L":         #p[0] indicates if each pizza tuple at index 0 matches for (L) Pizza
                pizzaCostL = 11.99
                allCostOfPizza.append(pizzaCostL)       # Appending the costL.
                print(f"Pizza {numberOfPiz[0]}: " + p[0] + "                 " + str(pizzaCostL))
                numberOfPiz.pop(0)          # This line will delete the number associated with each pizza and use the next appropriate number.
                for chosenTopps in p[1]: # This for loop checks the chosen toppings in pizzaOrder for (L pizza).
                    print(f"- {chosenTopps}")
                if len(p[1]) > 3:       # This condition checks if the user has picked more than three toppings on their L pizza.
                    topKeep = (len(p[1]) - 3) * 1.00        # If so it will calculate the total cost of the additional cost of toppings after the three chosen toppings!
                    addCostL = format(1.0, '.2f')
                    allCostOfToppings.append(topKeep)       # Appending the cost of toppings to the list
                    for x in range(0, len(p[1]) - 3):       # The additional toppings will be printed out!
                        print(f"Extra Topping ({p[0]})" + "          " + str(addCostL))
            if p[0] == "XL":    #p[0] indicates if each pizza tuple at index 0 matches for (XL) Pizza
                pizzaCostXL = 13.99
                allCostOfPizza.append(pizzaCostXL)      #Appending the costXL.
                print(f"Pizza {numberOfPiz[0]}: " + p[0] + "                 " + str(pizzaCostXL))
                numberOfPiz.pop(0)      # This line will delete the number associated with each pizza and use the next appropriate number.
                for chosenTopps in p[1]:        #This for loop will check the chosen toppings in pizzaOrder for (XL pizza)).
                    print(f"- {chosenTopps}")
                if len(p[1]) > 3:       # This condition checks if the user has picked more than three toppings on their XL pizza.
                    topKeep = (len(p[1]) - 3) * 1.25        # If so it will calculate the total cost of the additional cost of toppings after the three chosen toppings!
                    addCostXL = 1.25
                    allCostOfToppings.append(topKeep)   # Adding the cost of toppings to the list.
                    for x in range(0, len(p[1]) - 3):   # The additional toppings will be printed out!
                        print(f"Extra Topping (XL)" + "          " + str(addCostXL))

        totalCost = sum(allCostOfPizza) + sum(allCostOfToppings) # Will calculate the sum of total costs which icnludes extra toppping(s) and pizza(s).
        totalTax = round(TAXRATE * totalCost, 2) # Will calculate the sum of total tax of the pizza(s) and topping(s).
        print("Tax: " + "                      " + format(totalTax, '.2f'))
        finalCost = round((totalCost + totalTax), 2) # Will calcualte the sum of final cost including the total tax and the total cost!
        print("Total: " + "                    " + format(finalCost, '.2f'))



