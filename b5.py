import math

pt = int(input("Nhập số phần tử có trong danh sách: "))

A = []
kq = 0

for i in range(pt):
    A.append(int(input("Nhập phần tử: ")))

x = int(input("Nhập x = "))
for i in range(pt):
    can = round(math.sqrt(A[i]) * 1000) / 1000
    if can >= x :
        kq += 1

print("Có", kq, "phần tử lớn hơn", x)