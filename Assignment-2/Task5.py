credit=int(input("Enter your total credit:"))
Cgpa=float(input("Enter your CGPA:"))

if credit>30:
    if Cgpa>=3.80 and Cgpa<= 3.89:
        print("The student is eligible for a waiver of 25 percent")
    elif Cgpa>=3.90 and Cgpa<=3.94:
        print("The student is eligible for a waiver of 50 percent")
    elif Cgpa>=3.95 and Cgpa<=3.99:
        print("The student is eligible for a waiver of 75 percent")
    else:
      print("The student is eligible for a waiver of 100 percent")
else:
    print("The student is not eligible for a waiver")