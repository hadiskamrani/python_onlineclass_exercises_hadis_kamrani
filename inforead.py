import os
if os.path.exists('info.txt'):
    os.chdir('info.txt')
else:
    os.mkdir('info.txt')

with open(r'C:\Users\Hadis\Desktop\git-project1\info.txt', 'r') as info:
    text = info.read()
    print(text)