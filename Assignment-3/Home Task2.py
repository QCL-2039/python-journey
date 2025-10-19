def print_digit_num(num):
    if num == 0:
        return
    print_digit_num(num // 10)  
    print(num % 10, end=",")  

number = int(input("Enter your number: "))
print_digit_num(number)
