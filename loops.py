
#using for loop for counting and while loop for printing 10 numbers
#For loop example
print("This is the for loop example")
cart = ["tomatoes","potatoes","carrots","soup"]
count1 = 0
for items in cart:
    count1 += 1

print(count1)

#while loop example
print("This is the while loop example")
check = True
num1 = 0
while check:
    if num1 == 100:
        check = False
    else:
        num1 += 1
        print(num1)
