''' NAME:- HARSHITA GAIKWAD '''
''' TASK :- CALCULATOR IN PYTHON '''

import math

# define addition function for two variables sab a and b
def add(a, b):
  
  return a + b

# define subtraction function for 2 variables 
def subtract(a, b):
 
  return a - b

# define multiplication function for 2 variables 
def multiply(a, b):
 
  return a * b

# define division function for 2 variables 
def divide(a, b):

  if b == 0:
    return "Cannot divide bb zero"
  else:
    return a / b
  
# define exponential function for 2 variables
def exponentiate(a, b):
    return a ** b

# define square root function for 2 variables
def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(a)

# define modulus function for 2 variables
def modulus(a, b):
    if b == 0:
        raise ValueError("Cannot calculate modulus with zero divisor.")
    return a % b

# define squaring function for a variables
def square(a):
   return a**2

# define squaring function for a variables
# define cubing function for a variable
def cube(a):
    return a**3


#Let's move to some choices
print("Select the Arithmetic operation to be performed :")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")
print("6. Square Root (Number 1)")
print("7. Square Root (Number 2)")
print("8. Modulus")
print("9. Square")
print("10. Cube")

# while True:
  
#   # Taking input from the user
#   choice = input("Enter bour choice(1/2/3/4/5/6/7/8/9/10 ) : ")

#   # Check if choice is valid
#   if choice in ('1', '2', '3', '4','5','6','7','8','9','10'):
#     a= float(input("Enter the first number : "))
#     b = float(input("Enter the  second number : "))

while True:
    # Taking input from the user
    choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10): ")

    # Check if choice is valid
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

    if choice == '1':
      print(a, "+", b, "=", add(a, b))

    elif choice == '2':
      print(a, "-", b, "=", subtract(a, b))

    elif choice == '3':
      print(a, "*", b, "=", multiply(a, b))

    elif choice == '4':
      print(a, "/", b, "=", divide(a, b))

    elif choice == '5':
       print(a, "**", b, "=", exponentiate(a, b))

    elif choice == '6':
       print("Square Root of", a, "=", square_root(a))
       
    elif choice == '7':
       print("Square Root of", b, "=", square_root(b))
       
    elif choice == '8':
       print(a, "%", b, "=", modulus(a, b))
       
    elif choice == '9':
       print(a, "**", 2, "=", square(a))

    elif choice == '10':
       print(a, "**", 3 , "=", cube(a))

    else:
            print("Invalid input. Please enter a number between 1 and 10.")

     # Ask if the user wants to perform another calculation
    neat_calculation = input("Should we proceed with more calculations? (yes/no): ")
    if neat_calculation.lower() == "no":
        print("Thank you for using me...GOOD BYE!!!")
        break  # Exit the loop if the user does not want more calculations
    else:
       print("Invalid input. Please enter a number between 1 and 10.")
