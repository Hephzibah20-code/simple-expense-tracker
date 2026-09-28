# A program that calculates a user expense

user_name = input("Please, enter your name: ") # collects user name

while user_name .replace(" ", "").isalpha( ) == False: # check if user name has only letters, else it returns False
    print("Invalid name. Please enter a valid name.")
    user_name = input("Please, enter your name: ")    

# Asks a user to enter three expenses
expense_1 = float(input("Please, enter expense_1: ")) # asks user to input expense_1

while expense_1 <= 0 : #validates that expense_1 is greater than zero
    print("Invalid expense. Expense must be  greater than N0.")
    expense_1 = float(input("Please, enter expense_1: ")) # asks user to re-enter expense_1 after first failed attempt

expense_2 = float(input("Please, enter expense_2: ")) # asks user to input expense_2

while expense_2 <= 0: #validates that expense_2 is greater than zero
    print("Invalid expense. Expense must be greater than zero.") # asks user to re-enter expense_2 after first failed attempt
    expense_2 = float(input("Please, enter expense_2: "))

expense_3 = float(input("Please, enter expense_3: ")) # asks user to input expense_3

while expense_3 <= 0: #validates that expense_3 is greater than zero
    print("Invalid expense. Expense must be greter than 0.") # asks user to re-enter expense_3 after first failed attempt
    expense_3 = float(input("Please, enter expense+2: "))
    
# Calculates the total expense
total_expense = expense_1 + expense_2 + expense_3
print(total_expense) # displays the total expense of the user

# Average user expense
average_expense = total_expense / 3
print(round(average_expense, 2))

# Mesage to be displayed based on the total expense
if total_expense < 5000:
    print(f"{user_name}, your total expense is {total_expense}, which is less than N5000")
elif total_expense <= 10000:
    print(f"{user_name}, your total expense is {total_expense}, which is within the range of N5000 to N10000." )
else:
    print(f"{user_name}, your total expense is {total_expense}, which is above N10000.")

final_message = (f"{user_name}, your total expense spent is {total_expense}.")
print(final_message)