def highest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        highest = num1
    else:
        highest = num2
    return highest
        
firt_num = int(input("Enter the first number:"))
second_num = int(input("Enter the second number:"))
tercer_num = int(input("Enter the tercer number:"))
print("The highest number is " + str(highest_number(firt_num, second_num, tercer_num)))