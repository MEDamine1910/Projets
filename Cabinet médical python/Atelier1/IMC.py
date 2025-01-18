str1=input("Enter your body weight: ")
str2=input("Enter your height in cm: ")
weight=float(str1)
height=float(str2)/100
IMC=weight/(height**2)
print("Your weight is: ",weight)
print("Your height is: ",height)
print("Your IMC is: ",IMC)
if IMC<16.5:
    print("Underweight")
elif IMC>=16.5 and IMC<25:
    print("Normal")
elif IMC>=25 and IMC<30:
    print("Overweight")
else:
    print("Obese")
