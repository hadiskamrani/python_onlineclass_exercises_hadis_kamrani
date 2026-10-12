while True:
    try:
        adad = float(input("Yek adad vared kon: "))
        print("Adad motabar ast:", adad)
        break
    except ValueError:
        print("na motabar")