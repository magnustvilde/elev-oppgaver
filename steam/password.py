from random import choice as c
password, username = '', ''
for i in range (12):
    password += c('0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
    username += c('0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')

with open('users.txt','a') as f:
    f.write('PASSWORD: ' + password + '; USERNAME: ' + username + '\n')

with open('users.txt', 'r') as f:
    line = f.readline()
    password = line[10:10+12]
    username = line[-13:]
    print(password + ' ' + username)