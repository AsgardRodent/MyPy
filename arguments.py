
def print_name_age(name = "someone", age = "ancient"):
    print("hi my name is ", name ,"i am ", age, " years old")


print_name_age("gaurav", 20)
print_name_age("regigas")
print_name_age("supahotfire", 28)
print_name_age(age=32)

# to solve the above error u can directly replace the line(4) with the following code which just [rints all the data as itself

# print("hi my name is ", name ,"i am ", age , " years old") ----> this is to be replaced

# as a back up the default line is provided below :D
# print("hi my name is " + name + " i am " + str(age) + " years old")--------> default line

# in line(9) only 32 is passed which will be replaced by the name since it as per the definition/the parameters provided to the function
# so the keyword "None" is used to skip a parameter hence the new line will be :D
    # print_name_age(None,32) ------> new line
    # print_name_age(32)---------> default line
    # none --> bool
# this error can be sorted using key arguments like #print_name_age(age = 32)
# REMEMBER KEY ARGUMENTS CAN BE PASSED IN ANY MANNER AS YOU LIKE ,SINCE THEY ARE DEFINED TO A SPECIFIC VALUE
