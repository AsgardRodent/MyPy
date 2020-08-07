#largestnnumberwithfunction
######################################################

def max(x,y):
    if x >= y:
        return x
    else:
        return y

num1 =int(input("enter first value"))
num2 =int(input("enter second value"))
num3 =int(input("enter third value"))

maxnumber1 = max(num1,num2)
maxnumber2= max(maxnumber1,num3)

print(max(maxnumber1,num3)," is the greatest number")
