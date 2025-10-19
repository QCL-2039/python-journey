quantity = int(input("Enter your number size: "))

maximum= int(input("Enter number 1:"))
minimum=maximum
sum=maximum
for i in range(1, quantity):
    a = int(input(f"Enter number {i + 1}: "))
    sum+=a

    if a > maximum:
        maximum = a
    if a < minimum:
        minimum=a
print("Maximum is:", maximum)
print("Minimum is:",minimum)
print("Average is:",sum/quantity)