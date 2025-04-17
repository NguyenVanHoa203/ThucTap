def convert_temperature():
    temp = float(input("Nhập nhiệt độ: "))    
    unit = input("Đơn vị hiện tại (C/F): ").upper() 

    if unit == "C":
        converted = (temp * 9/5) + 32
        print(f"{temp}°C = {converted:.2f}°F")
    elif unit == "F":
        converted = (temp - 32) * 5/9
        print(f"{temp}°F = {converted:.2f}°C")
    else:
        print("Đơn vị không hợp lệ.")
