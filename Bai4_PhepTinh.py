def calculator():
    print("Máy tính đơn giản")
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    op = input("Chọn phép toán (+, -, *, /): ")

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b != 0:
            result = a / b
        else:
            return "❌ Không thể chia cho 0!"
    else:
        return "⚠️ Phép toán không hợp lệ."

    return f"Kết quả: {result}"

print(calculator())
