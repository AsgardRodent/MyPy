print("Welcome To Jumanji!!")
print("Make Sure To Check If You Are Eligible For the Ride or Not")
User_height = int(input("Enter Your Height => "))
User_Age = int(input("Enter Your Age => "))
if User_height > 120:
    
    if User_Age < 12:
        print("Welcome Aboard! Please Pay 5$ to the Monkey At The Reception")
        bill = 5
        choice = input("Would you like to take Photos? (Y/N) => ")
        if choice.lower() in ["y", "yes"]:
            bill += 3
            print("Your Total Bill is: $" + str(bill))
        elif choice.lower() in ["n", "no"]:
            print("Your Total Bill is :$" + str(bill))

    elif User_Age < 18:

        print("Welcome Aboard! Please Pay 7$ to the Monkey At The Reception")
        bill = 7
        choice = input("Would you like to take Photos? (Y/N) => ")
        if choice.lower() in ["y", "yes"]:
            bill += 3
            print("Your Total Bill is: $" + str(bill))
        elif choice.lower() in ["n", "no"]:
            print("Your Total Bill is :$" + str(bill))
    
    elif User_Age < 45:

        print("Welcome Aboard! Please Pay 12$ to the Monkey At The Reception")
        bill = 12
        choice = input("Would you like to take Photos? (Y/N) => ")
        if choice.lower() in ["y", "yes"]:
            bill += 3
            print("Your Total Bill is: $" + str(bill))
        elif choice.lower() in ["n", "no"]:
            print("Your Total Bill is :$" + str(bill))
    elif 45< User_Age < 55:
        print("Welcome Aboard! You Ride For Free!!!!")
        bill = 0
        choice = input("Would you like to take Photos? (Y/N) => ")
        if choice.lower() in ["y", "yes"]:
            bill += 3
            print("Your Total Bill is: $" + str(bill))
        elif choice.lower() in ["n", "no"]:
            print("Your Total Bill is :$" + str(bill))
else:
    {
        print("See you in a few years !! Train Well To Tackle The Jungle")
    }