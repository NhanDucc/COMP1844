import numpy as np
import matplotlib.pyplot as plt

def DrawBox(x, y, size, r, g, b):
    for i in range(int(size)):
        plt.plot([x, x + size], [y + i, y + i], '#{:02x}{:02x}{:02x}'.format(r, g, b))

# Dữ liệu nhiệt độ cho 7 thành phố
Cities = np.array([
    [6, 8, 11, 16, 21, 25, 27, 26, 23, 17, 10, 6],
    [4, 6, 12, 17, 21, 25, 28, 27, 23, 17, 11, 6],
    [9, 11, 13, 15, 18, 21, 23, 23, 21, 17, 13, 9],
    [-2, 1, 5, 9, 14, 20, 23, 21, 17, 10, 3, -2],
    [-2, 1, 4, 10, 15, 21, 24, 23, 19, 12, 7, 1],
    [1, 2, 6, 12, 17, 22, 25, 24, 20, 14, 8, 3],
    [15, 17, 19, 22, 25, 27, 27, 27, 26, 23, 20, 17]
], dtype=int)

Min = np.min(Cities)
Max = np.max(Cities)
Threshold = 10  # Ngưỡng giá trị

# Cấu hình đồ thị
plt.axis([0, 600, 0, 400])
plt.xticks([])
plt.yticks([])
BoxSize = 40
OffsetX, OffsetY = 15, 12

# Vẽ heat map
for i in range(Cities.shape[0]):
    for j in range(Cities.shape[1]):
        value = Cities[i, j]
        if value <= Threshold:
            ColourCode = int(((Threshold - value) / (Threshold - Min)) * 255)  # Màu xanh đậm hơn khi giá trị nhỏ
            DrawBox(60 + BoxSize * j, 300 - BoxSize * i, BoxSize, 0, 0, ColourCode)
        else:
            ColourCode = int(((value - Threshold) / (Max - Threshold)) * 255)  # Màu đỏ tăng dần
            DrawBox(60 + BoxSize * j, 300 - BoxSize * i, BoxSize, ColourCode, 0, 0)
        plt.text(OffsetX + 60 + BoxSize * j, OffsetY + 300 - BoxSize * i, str(value), color='#FFFFFF')

# Vẽ thang màu (blue → red)
for i in range(280):
    if i < 140:
        ColourCode = int(((140 - i) / 140) * 255)  # Xanh đậm đến nhạt dần
        plt.plot([560, 580], [i + 60, i + 60], '#{:02x}{:02x}{:02x}'.format(0, 0, ColourCode))
    else:
        ColourCode = int(((i - 140) / 140) * 255)  # Đỏ nhạt đến đậm
        plt.plot([560, 580], [i + 60, i + 60], '#{:02x}{:02x}{:02x}'.format(ColourCode, 0, 0))

plt.text(585, 58, str(Min))
plt.text(585, 335, str(Max))

# Nhãn tháng
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for idx, month in enumerate(months):
    plt.text(72 + idx * 40, 20, month)

# Nhãn thành phố
cities = ['Phoenix', 'Little Rock', 'Sacramento', 'Denver', 'Hartford', 'Dover', 'Tallahassee']
for idx, city in enumerate(cities):
    plt.text(5, 315 - idx * 40, city)

plt.show()
