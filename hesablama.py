def hesablama():
    name = input("Malın adını yazın: ")
    price = float(input("Malın qiymetin yazin: "))
    weight = float(input("Malın çəkisini yazın: "))
    discount = int(input("Endirim faizini qeyd edin: "))
    summary = price * weight - (price * weight * discount / 100)
    print(f"{name} umumi deyeri: {summary} : 'AZN' ")
hesablama()