a =int(input("Enter the grade of Science :"))
b =int(input("Enter the grade of Maths: "))
c =int(input("Enter the grade of English: "))
d =int(input("Enter the grade of Nepali: "))
x = (a+b+c+d)/4
print(x)
if (x>=90 and x<100):
    print("You have passed with A+ Grade")
elif (x>=80 and x<90):
    print("You have passed with A Grade")
elif (x>=70 and x<80):
    print("You have passed with B+ Grade")
elif (x>=60 and x<70):
    print("You have passed with B Grade")
elif (x>=50 and x<60):
    print("You have passed with C+ Grade")
elif (x>=40 and x<50):
    print("You have passed with C Grade")
else:
    print("You have Failed")