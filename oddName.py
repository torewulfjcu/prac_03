"""Tore"""

name = input("Enter name: ")
while not name:
    print("Try again!")
    name = input("Enter name: ")

for i in range(0, len(name), 2):
    print(name[i])

