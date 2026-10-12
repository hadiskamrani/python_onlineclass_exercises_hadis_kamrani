try:
    meghdar1 = int(input("adad vared kon: "))
    meghdar2 = int(input("adad vared kon: "))
    result = meghdar1 / meghdar2
    print(result)
except ZeroDivisionError:
    print("meghdar2 nemitavanad 0 bashad")
    