def is_prime(n):
    if n < 2: return False  # Số < 2 không phải số nguyên tố
    for i in range(2, int(n**0.5)+1):  # Kiểm tra từ 2 đến căn bậc 2 của n
        if n % i == 0: return False
    return True
