print("~~~~~~~~~~WELCOME TO BMI CALCULATOR~~~~~~~~~~~~~~")
User_Weight = float(input("Enter Your Weight(kg) => "))
User_Height = float(input("Enter Your Height(m) => "))

Bmi = User_Weight / (User_Height**2)

if Bmi <= 18.5:
    print(" Your BMI is " + str(round(Bmi,5)) + " You Are UnderWeight")
elif 18.5 < Bmi <=25:
    print(" Your BMI is " + str(round(Bmi,5)) + " You Have A Normal Weight")
elif 25 < Bmi <=30:
    print(" Your BMI is " + str(round(Bmi,5)) + " You Are Slightly OverWeight")
elif 30 < Bmi <=35:
    print(" Your BMI is " + str(round(Bmi,5)) + " You Are Obese")
else:
    print(" Your BMI is " + str(round(Bmi,5)) + " You Are Clinically Obese")
