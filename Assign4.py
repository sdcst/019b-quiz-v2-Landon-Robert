#!python3
"""
Billy is inviting people to his party. He is accepting requests
from his friends, but only wants to send 1 invitation out per
person. He decides to store names in a list, and only add the
ones that are not already there. Can you help a brother out?

Your program should keep asking the user to enter in a name 
(first and last). If the name is not on the list, add it,
otherwise say "That name is already on the list".

if the user enters in a blank line, then stop the input.
Sort the list of names (it will be sorted by first name)
and print out all of the names on the list. Also print out
the number of names on the list so he knows how many 
invitations to send.

This program will require you to incorporate everything we
have learned so far.
"""

names = []
x = 1
for i in range(x):
    name = input("Enter a name (First and Last): ")
    if name != None:
        names.append(name)
        x = x + 1
    elif name in names:
        print("That name is already on the list.")
        x = x + 1
names.sort()
y = names.index(-1)
print(names)
print(f"There are {y} names on the list.")

