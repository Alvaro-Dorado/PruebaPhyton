#Esto es una funcion
def lower_num(num1,num2):
    if num1 <= num2:
        lowest = num1
    else:
        lowest = num2

#Esto es uan llamada a una funcion
firt_num = int(input("Enter the first number:"))
second_num = int(input("Enter the second number:"))

print("The lowest number is " + str(lower_num(firt_num, second_num)))

