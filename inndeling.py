import random
elever = ['David',
'Even',
'Magnus S.N.',
'Morten',
'Sindre',
'Umair',
'Vetle',
'Diego',
'Andreas',
'Hamid',
'Iselin',
'Jack ',
'Juni',
'Magnus P.S.',
'Magnus P.O.',
'Sigurd',
'Sondre',
'Theodor',
'Sander',
'Chris',
'Henrik',
'Isak T.D.',
'Jacky',
'Joachim',
'Syver',
'Aron',
'Ola',
'Amir',
'Daniel',
'Fillip',
'Isak O.J.',
'Isak S.S.',
'Kristian',
'Nicolai',
'Nicolay',
'Bror Viktor']

gruppe1,gruppe2 = [], []
for i in range(16):
    
    gruppe1 = random.choices(elever,k=16)
for elev in elever:
    if elev not in gruppe1:
        gruppe2.append(elev)

print(gruppe1)
print(gruppe2)

print('Ola' in gruppe1)
print('Sander' in gruppe1)
print('Sondre' in gruppe1)
print('Chris' in gruppe1)
