import math

pt = int(input("Nhập số phần tử có trong danh sách: "))

A = []
Kq = []

for i in range(pt):
    A.append(int(input("Nhập phần tử: ")))

TBC = float(input("Nhập trung bình căn: "))

for i in range(pt):
    can = round(math.sqrt(A[i]) * 1000) / 1000
    if can > TBC:
        Kq.append(can)

print(Kq)