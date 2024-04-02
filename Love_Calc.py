print("Welcome To Love Calculator")
Name1 = input()
Name2 = input()
combined_name = Name1+Name2
Lower_combined_name = combined_name.lower()

Check_string_1 = "true"
Check_string_2 = "love"
Count1 = 0
Count2 = 0
for char in Lower_combined_name:
    if char in Check_string_1:
        Count1 += 1

    if char in Check_string_2:
        Count2 +=1

Score = str(Count1)+str(Count2)
Score = int(Score)

if (10 > Score) or (Score > 90):
    print("Your Love Score is :" + str(Score) + "%, You Go together like Coke & mentos")
elif (40 <= Score) and (Score <= 50):
    print("Your Love Score is :" + str(Score) + "%, You Are Alright Together")
else:
    print("Your Love Score is :" + str(Score) + "%")