def calculate_sum(number):
  #Calculates the sum of all numbers from 1 to the given number.6

  # Initialize a variable to store the sum
  total_sum = 0

  # Loop through numbers from 1 to the input number
  for i in range(1, number + 1):
    # Add the current number to the total sum
    total_sum += i

  return total_sum

# Get the user's input
number = int(input("Enter a number: "))

# Calculate the sum
sum_of_numbers = calculate_sum(number)

# Print the sum
print(f"The sum of numbers from 1 to {number} is: {sum_of_numbers}")