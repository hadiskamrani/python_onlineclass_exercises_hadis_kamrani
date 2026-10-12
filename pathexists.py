import os
main_path = r"C:\Users\Hadis\Desktop\git-project1\info.txt"
 
if os.path.exists(main_path):  
    os.chdir(main_path)
    
else:
    os.mkdir(main_path)
    os.chdir(main_path)