def calculate_monthly_salary(annual_salary):
  #Calculates the monthly salary from the annual salary with rounding up.6

  # Divide the annual salary by 12 and add 0.5 for rounding up
  monthly_salary = int(annual_salary / 12 + 0.5)
  return monthly_salary

# Get the user's annual salary input
annual_salary = float(input("Enter your annual salary: "))

# Calculate the monthly salary
monthly_salary = calculate_monthly_salary(annual_salary)

# Print the monthly salary
print(f"The monthly salary is {monthly_salary}.")