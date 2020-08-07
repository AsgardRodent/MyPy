#calc
c = int
def addition(x,y):
    c  = x+y
    return c

def sub(x,y):
    c = x-y
    return c

def mult(x,y):
    c =x * y
    return c

def divide(x,y):
    c = x/y
    return c

print("welcome to my python calc")
print("what operation would you like to perform on two numbers ?")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice here :: ")
    if choice in ('1','2','3','4'):
        x = int(input("Enter first number"))
        y = int(input("Enter second number"))

        if choice  == '1':
            print(x,"+",y,"=",addition(x,y))
        elif choice == '2':
            print(x,"-",y,"=",sub(x,y))
        elif choice == '3':
            print(x,"*",y,"=",mult(x,y))
        elif choice == '4':
            print(x,"/",y,"=",divide(x,y))
        break
    else:
        print("invalid choice")