def categorize_number(number):
  #Categorizes a number based on its value.

  if number < 100:
    return "Small"
  elif number > 200:
    return "Large"
  else:
    return "Medium"

# Get the user's input
number = int(input("Enter a number: "))

# Call the function to get the category
category = categorize_number(number)

# Print the category
print(f"The number {number} is categorized as {category}.")