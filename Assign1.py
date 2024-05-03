#!python3
# Write a program that uses a for loop to ask the user to enter
# in 5 numbers.  The program will determine the sum of the 5 numbers
# and calculate the average
# You must use only 1 input statement in your program
Num = 0
Sum = 0
for i in range(5):
    Num = float(input("Enter a number: "))
    Sum = Sum + Num
print(f"The sum of the numbers is {Sum}")