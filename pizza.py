print("Thank You For Choosing Hungund's Oven")
Size = input("What Size Pizza Would You Like To Order? (S/M/L) => ")
Pep_option = input("Would You like to Add Pepperoni? (Y/N) => ")
Cheese_option = input("Would You Like to Add Extra Cheese? (Y/N) => ")

# Initialize amount based on pizza size
if Size.lower() == "s" or Size.lower() == "small":
    Amount = 15
elif Size.lower() == "m" or Size.lower() == "medium":
    Amount = 20
elif Size.lower() == "l" or Size.lower() == "large":
    Amount = 25
else:
    print("Invalid pizza size selected. Please choose S, M, or L.")
    exit()

# Add additional charges for toppings
if Pep_option.lower() == "y" or Pep_option.lower() == "yes":
    Amount += 2
if Cheese_option.lower() == "y" or Cheese_option.lower() == "yes":
    Amount += 1

print("Thank You For Choosing Hungund's Oven, Your total is: $" + str(Amount))
