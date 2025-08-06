class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

answer = input("WHich parrot do you want to learn about? (Blu/Woo):")

if answer == "Blu" or answer == "blu" or answer == "BLU":
    print("{} is a {}".format(blu.name, blu.species))
    print("{} is {} years old".format(blu.name, blu.age))
elif answer == "woo" or answer == "Woo" or answer == "WOO":
    print("{} is a {}".format(woo.name, woo.species))
    print("{} is {} years old".format(woo.name, woo.age))
else:
    print("We don't know that parrot")