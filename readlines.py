
import os

file_path = r'C:\Users\Hadis\Desktop\git-project1\info.txt'

if os.path.isfile(file_path):
    with open(file_path, 'r') as info:
        text_list = info.readlines()

    count_line = 0
    count_word = 0
    count_ch = 0

    for line in text_list:
        count_line += 1
        for word in line.split():
            count_word += 1
            for ch in word:
                count_ch += 1

    print('Lines:', count_line)
    print('Words:', count_word)
    print('Characters:', count_ch)
else:
    print('File not found!')