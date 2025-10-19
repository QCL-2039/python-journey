# Write a Python program to compute and display a person's weekly salary as determined by the
# following conditions:
# • Ifthe hours worked is less than or equal to 40, then the person receives Tk 200 per hour.
# • Ifthe hours worked is greater than 40, then the person receives Tk 8000 plus Tk 300 for
# each hour worked over 40 hours.
# The program should request the hours worked as an input from the user and display the salary as
# output. You need to make sure that user input is valid. For example, a person cannot work for -5
# hours or more than 168 hours in a week. So, the valid hours range is 0 to 168. For invalid hours,
# print outputs as given in the samples below.
# Hint: you can consider the hour (user input) to be an integer

worked_hours=int(input("Enter the total worked hour:"))

if worked_hours<0:
    print(" Hour can not be negative")
elif worked_hours<=40 and worked_hours>0:
    print("Salary is:",worked_hours*200)
elif worked_hours>40 and worked_hours<168:
    print("Salary is:",(8000+ (worked_hours-40)*300))
else:
    print(" Impossibletoworkmorethan168hoursweekly")