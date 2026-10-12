i = 0
try:
    with open(r'C:\Users\Hadis\Desktop\git-project1\adad.txt',"r") as adad:
        for i in adad:
            i = i + 1
        print(i)
except ValueError:
    print("khata")        