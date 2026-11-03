import math

pt = int(input("Nhập số phần tử có trong danh sách: "))

kq = 0

for i in range(pt):
    kq += round(math.sqrt(int(input("Nhập phần tử: "))) * 1000) / 1000

print(kq)