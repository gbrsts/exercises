# Write a program that reads an employee's number, his/her worked hours number in a month and the amount he received per hour. 
# Print the employee's number and salary that he/she will receive at end of the month, with two decimal places.

a, b, c = map(int, input().split(" "))

salary = (b * c)

print(f"NUMBER = {a}")
print(f"SALARY = {salary:.2f}")