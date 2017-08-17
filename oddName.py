"""Tore"""

def main():
    name = get_name()
    letter_frequency = get_frequency()
    print_name(name, letter_frequency)


def print_name(name, letter_frequency):
    for i in range(0, len(name), letter_frequency):
        print(name[i])


def get_name():
    name = input("Enter name: ")
    while not name:
        print("Try again!")
        name = input("Enter name: ")
    return name

def get_frequency():
    letter_frequency = int(input("Enter frequency: "))
    return letter_frequency


main()