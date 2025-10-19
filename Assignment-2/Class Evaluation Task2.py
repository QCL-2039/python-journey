#  Write the Python code of a program that finds the number of hours, minutes, and seconds in a
#  given number of seconds. The number of seconds is taken as input from the user.
#  hint(1): This is not a branching problem. We may consider our user input to be an integer value
#  and use just // and % operators to solve the problem
#  hint(2): 1 hour = 60 minutes = 3600 seconds and 1 minute = 60 seconds

total_Seconds=int(input("Enter the total seconds:"))

hours=total_Seconds//3600
print("Hours:",hours)
minutes=(total_Seconds%3600)//60
print("Minutes:",minutes)
seconds=(total_Seconds%3600)%60
print("Seconds:",seconds)
