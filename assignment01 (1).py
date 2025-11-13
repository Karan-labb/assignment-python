num1 = float(input("enter your first number: "))
num2 = float(input("enter your second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1/num2 if num2 != 0 else "cannot divide by zero"
print(addition)
print(subtraction)
print(multiplication)
print(division)