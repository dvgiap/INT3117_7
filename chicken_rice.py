def calculate_total_price(x, y):
    meal_price = 50000

    if x < 1 or x > 10 or y < 0 or y > 10:
        print("Input khong hop le")
        return
    elif y == 0:
        total_price = meal_price * x
    elif 0 < y <= 2:
        total_price = meal_price * x + 10000
    else:
        total_price = meal_price * x + 10000 + (y - 2) * 5000
    
    return total_price

x = int(input("Nhap so suat com ga (1-10): "))
y = float(input("Nhap khoang cach (km) (0-10): "))

total_price = calculate_total_price(x, y)

print(f"Tong so tien can phai tra: {total_price} VND")
