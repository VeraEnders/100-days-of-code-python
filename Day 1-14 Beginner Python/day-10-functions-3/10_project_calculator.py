# Calculator

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}


num1 = float(input("What's the first number? "))

while True:
  operation_symbol = input(f"Pick an operation (+, -, * or /): ")

  num2 = float(input("What's the next number? "))
  calc_func = operations[operation_symbol]
  answer = calc_func(num1, num2)

  print(f"{num1} {operation_symbol} {num2} = {answer}")
  should_continue = input(f"Type 'y' to continue calculating with {answer}, type 'n' to exit: ").lower()

  if should_continue == 'y':
    num1 = answer
  else:
    print("Goodbye.")
    break