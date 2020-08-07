number = int(input("Enter the number: "))
count = 0
for x in range(2,number):
    if number % x == 0:
        count = count + 1
if count == 0:
    print("number is prime")
else:
    print("number is not prime")