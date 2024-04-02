print("~~~~~~~~~~~~~~~~~~Welcome To Leap Year Checker!!~~~~~~~~~~~~~~~~~~~")
year = int(input("Enter The Year => "))

if year % 4 == 0 and year % 100 == 0:
    if year % 400 == 0:
        print("Leap Year")
else:
    print("Not A leap year")