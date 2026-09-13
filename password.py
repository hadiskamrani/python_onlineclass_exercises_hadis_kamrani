password = "admin1234"
passwordet = input("passworde khood ra vared konid ").lower()
for i in range(3):
    if password != passwordet:
        print("passwordet sahih nis")
        passwordet = input("passworde khood ra vared konid ").lower()
        break
        print("hesabe shooma masdood shood") 
    else:
        print("vorode movafagh")
        break
       