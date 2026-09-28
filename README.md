# Simple Expense Tracker 

## Project Overview 
A beginner Python program that collects three expenses, validates the values entered, 
calculates the total and average expense, and categorizes total spending into three ranges. 

## Features 
- Collects and validates the user's name 
- Collects three expense amounts 
- Prevents zero or negative expenses 
- Calculates total expenses 
- Calculates average expense 
- Rounds the average to two decimal places 
- Categorizes total spending using `if`, `elif`, and `else` 
- Displays a final message containing the user's name 

## Spending Categories 
| Total Expense | Category | 
|---|---| 
| Below ₦5,000 | Less than ₦5,000 | 
| ₦5,000–₦10,000 | Within the ₦5,000–₦10,000 range | 
| Above ₦10,000 | Above ₦10,000 | 

## Python Concepts Used 
- Variables - `input()` 
- Type conversion with `float()` 
- Strings and string methods 
- `.replace()` 
- `.isalpha()` 
- `.title()` 
- `while` loops 
- `if`, `elif`, and `else` 
- Comparison operators 
- Logical operators 
- f-strings 
- Basic arithmetic 
- `round()` 

## Program Flow 
Get user's name   
↓   
Validate user's name   
↓   
Get Expense 1   
↓   
Validate Expense 1   
↓   
Get Expense 2   
↓   
Validate Expense 2   
↓   
Get Expense 3   
↓   
Validate Expense 3   
↓   
Calculate total expense   
↓   
Calculate average expense   
↓   
Round average to 2 decimal places   
↓   
Check total expense range   
↓   
Display spending message   
↓   
Display final message with user's name   
↓   
End 

## Example 
Example input: 
- Expense 1: ₦3,000 
- Expense 2: ₦700 
- Expense 3: ₦4,000 
The program calculates: 
- Total: ₦7,700 
- Average: ₦2,566.67 
The total falls within the **₦5,000 – ₦10,000** range. 

## What I Learned 
This project helped me practise input validation, `while` loops, conditional statements, 
calculations, string methods, type conversion, and formatted output. 
I also practised reusing concepts from an earlier project and debugging variable reassignment 
inside validation loops. 

## Challenges 
One challenge was making sure invalid expense values were rejected and the user was asked 
to enter a valid value again. 
Another challenge was understanding that a new input inside a loop must be assigned back to 
the correct variable. 

## Future Improvements 
- Add error handling for non-numeric expense inputs 
- Allow users to enter more than three expenses 
- Store expense records 
- Improve the output formatting 

## Project Status 
Completed beginner Python project. 
