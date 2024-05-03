#!python3
"""
Fix this program.
It should ask the user to enter in 10 numbers and see
if the number is positive or negative
"""
for n in range(10):
    Input = int(input("Enter an Integer: "))
    if Input > 0:
        print('that is a positive number')
    elif Input < 0:
        print('that is a negative number')
