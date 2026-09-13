import random
adad_tasadoofi = random.randint(1,100)
number = int(input("adad bein 0 ta 100 vared konid "))
for i in range(1,101):
    if adad_tasadoofi == number:
        print("doroste")
        break
    elif adad_tasadoofi > number:
        print("adad ra bozorgtar kon")
        number = int(input("adad bein 0 ta 100 vared konid "))
        
    elif adad_tasadoofi < number:
        print("adad ra kochektar kon")
        number = int(input("adad bein 0 ta 100 vared konid "))
        