def divide_and_round(number):
  #Divides a number by 3 and rounds the result to three decimal places.

  # Use round function with 3 as the number of decimal places
  result = round(number / 3, 3)
  return result

# Get the user's input as an integer
number = int(input("Enter a whole number: "))

# Call the function to divide and round
result = divide_and_round(number)

# Print the result
print(f"The result is: {result}")