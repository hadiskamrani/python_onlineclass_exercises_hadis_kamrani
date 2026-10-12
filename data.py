data = [1,2,3]
try:
    index = int(input("andis vared konid"))
    print('ozv mored nazar:', data[index])
except ValueError:
    print("adad sahih vared konid")
except IndexError:
    print("andis kharej az mahdoode ast")