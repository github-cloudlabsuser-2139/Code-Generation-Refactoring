#A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases

MAX = 100

def calculate_sum(arr):
   result = 0
   for num in arr:
      result += num
   return result

def main():
   try:
      n = int(input("Enter the number of elements (1-100): "))
      if not 1 <= n <= MAX:
            print("Invalid input. Please provide a digit ranging from 1 to 100.")
            exit(1)

      arr = []

      print(f"Enter {n} integers:")
      for _ in range(n):
            try:
               arr.append(int(input()))
            except ValueError:
               print("Invalid input. Please enter valid integers.")
               exit(1)

      total = calculate_sum(arr)

      print("Sum of the numbers:", total)

   except KeyboardInterrupt:
      print("\nProgram terminated by user.")
      exit(1)

if __name__ == "__main__":
   main()

      # A refactored program to calculate the sum of user-provided integers.
   
   MAX_ELEMENTS = 100
   
   def calculate_sum(arr):
       """Calculate the sum of elements in the array."""
       return sum(arr)
   
   def get_valid_integer(prompt):
       """Prompt the user for a valid integer input."""
       while True:
           try:
               return int(input(prompt))
           except ValueError:
               print("Invalid input. Please enter a valid integer.")
   
   def main():
       """Main function to execute the program."""
       print("Welcome to the Sum Calculator!")
   
       # Get the number of elements
       n = get_valid_integer(f"Enter the number of elements (1-{MAX_ELEMENTS}): ")
       if not 1 <= n <= MAX_ELEMENTS:
           print(f"Invalid input. Please provide a number between 1 and {MAX_ELEMENTS}.")
           return
   
       # Get the elements
       arr = []
       print(f"Enter {n} integers:")
       for i in range(n):
           arr.append(get_valid_integer(f"Element {i + 1}: "))
   
       # Calculate and display the sum
       total = calculate_sum(arr)
       print("Sum of the numbers:", total)
   
   if __name__ == "__main__":
       try:
           main()
       except KeyboardInterrupt:
           print("\nProgram terminated by user.")
