from random import randint as r

to_dim = [[0,1,2],[3,4,5],[6,7,8], [9,10,11]]

# itererer over den to-dimensjonale listen vha.
# indeks og gjør om til tilfeldige tall
for i in range(len(to_dim)):
    for j in range(len(to_dim[i])):
        to_dim[i][j] = r(0,100)

# itererer over den to-dimensjonale listen vha. indeks og skriver ut tallene
for i in range(len(to_dim)):
    streng = ''
    for j in range(len(to_dim[i])):
        # print(to_dim[i][j])
        streng += str(to_dim[i][j]) + '\t'
    print(streng)

# itererer over den to-dimensjonale listen direkte og skriver ut tallene
# for elem in to_dim:
#     # print(elem)
#     streng = ''
#     for item in elem:
#         streng += str(item) +'\t'
#     print(streng)