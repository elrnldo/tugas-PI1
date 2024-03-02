total_sum = 0  # Initialize a variable to store the sum of number
number = 0  # Initialize a variable to store the inputted number

while number != -1:
  # Get the user's input
  number = int(input("Enter a number (or -1 to stop): "))

  # Add the number to the total sum if it's not -1
  if number != -1:
    total_sum += number

# Print the final sum
print(f"The sum of all entered numbers is: {total_sum}")