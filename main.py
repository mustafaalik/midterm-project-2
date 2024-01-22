# Function to calculate the factorial of a given number
def calculate_factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result

# Function to multiply two numbers and return the result
def multiply_numbers(a, b):
    return a * b

# Function to divide two numbers and return the quotient
def divide_numbers(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "Error: Cannot divide by zero"

# Example usage
input_number = int(input("Enter a number to calculate its factorial: "))
factorial_result = calculate_factorial(input_number)
print(f"The factorial of {input_number} is: {factorial_result}")

num1 = float(input("Enter the first number to multiply: "))
num2 = float(input("Enter the second number to multiply: "))
multiply_result = multiply_numbers(num1, num2)
print(f"The product of {num1} and {num2} is: {multiply_result}")

dividend = float(input("Enter the dividend for division: "))
divisor = float(input("Enter the divisor for division: "))
divide_result = divide_numbers(dividend, divisor)
print(f"The quotient of {dividend} divided by {divisor} is: {divide_result}")
