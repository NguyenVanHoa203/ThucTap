def analyze_string(s):
    letters = digits = specials = 0
    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        else:
            specials += 1
    print(f"🔤 Chữ cái: {letters}")
    print(f"🔢 Chữ số: {digits}")
    print(f"🔣 Ký tự đặc biệt: {specials}")
