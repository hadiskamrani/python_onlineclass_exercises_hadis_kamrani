def safe_int(value):
    try:
        return int(value)
    except TypeError:
        print("type monaseb vared konid")
    except ValueError:
        print("int vared konid")

zarf = safe_int("123")
print(zarf)  