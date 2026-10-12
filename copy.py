file_path = r'C:\Users\Hadis\Desktop\git-project1\info.txt'
file_pat = r'C:\Users\Hadis\Desktop\git-project1\info1.txt'

with open(file_path, "r") as info:
    x = info.read()

with open(file_pat, "w") as info1:
    info1.write(x.upper())