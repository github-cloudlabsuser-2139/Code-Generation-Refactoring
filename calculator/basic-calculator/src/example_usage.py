from calculator import Calculator

# Create an instance of the Calculator class
calc = Calculator()

# Perform calculations
result_add = calc.add(10, 5)         # 10 + 5 = 15
result_subtract = calc.subtract(10, 5)  # 10 - 5 = 5
result_multiply = calc.multiply(10, 5)  # 10 * 5 = 50
result_divide = calc.divide(10, 5)      # 10 / 5 = 2.0

# Print results
print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")