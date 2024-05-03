"""
Write a program that uses a for loop.
Each iteration will ask the user to enter a name
Add the input to the provided list
"""
names = []
x = int(input("Enter the number of names: "))
for i in range(x):
    name = str(input(f"Enter name {i+1}: "))
    names.append(name)
print(names)