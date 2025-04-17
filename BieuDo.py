import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 6]
plt.plot(x, y, color='green', marker='o')
plt.title("Biểu đồ tuyến tính")
plt.xlabel("Trục X")
plt.ylabel("Trục Y")
plt.grid(True)
plt.show()