from random import choice as c
students = [
    'Vetle', 'Sindre', 'Magnus S.N.',
    'Syver ', 'Sander', 'Jacky', 'Chris',
    'Isak T.D.', 'David', 'Aron',
    'Diego', 'Joachim', 'Morten'
    ]

def makeOrder(persons):
    order = []
    while students:
        student = c(students)
        students.remove(student)
        order.append(student)
    return order

def printOrder(persons):
    for i in range(len(persons)):
        input(f'Candidates left: {len(persons)-i}\nShow next candidate with Enter:')
        print(f'Candidate: {persons[i]}')

order = makeOrder(students)
printOrder(order)
