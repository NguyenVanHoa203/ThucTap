import math

# Nhập hệ số a, b, c
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Tính delta (bình phương biệt thức)
delta = b**2 - 4*a*c


# Giải phương trình
if a == 0:
    if b == 0:
        print("Phương trình vô nghiệm." if c != 0 else "Phương trình vô số nghiệm.")
    else:
        x = -c / b
        print(f"Phương trình bậc nhất có nghiệm: x = {x}")
else:
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {x}")
    else:
        print("Phương trình vô nghiệm.")
