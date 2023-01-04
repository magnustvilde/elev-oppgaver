import random

person = [
"Henrik", "Jacky", "Sander", "Chris", "Amir", "Ola", "Isern", "Magnus (Smagga)", "Juni", "Izzi",
"Aron", "Andreas", "Magnus P.O", "Theodor", "Sigurd", "Kristian", "Umair", "Fillip", "Daniel","David","Diego",
"Even","Hamid","Isak S.S.", "Isak T.D.", "Jack", "Joachim", "Magnus S.N.", "Morten", "Nicolai", "Nicolay", "Sindre", "Sondre", "Syver", "Vetle", "Viktor",]

print(person)

my_choices = []
d = 35

while len(person):
    # x = input("")
    random_choice = random.randint(0, d)
    valg = person.pop(random_choice)

    my_choices.append(valg)

    if d <= 33:
        print("\n\n", my_choices[-2], "->", valg)
    elif d <= 34:
        print("\n\n", my_choices[-0], "->", valg)
    elif d == 35:

        print("\n\n", valg)


    print(len(person))
    print(my_choices)
    d -= 1
