import math

pt = int(input("Nhập số phần tử có trong danh sách: "))

A = []
a = int(input("Nhập a = "))
b = int(input("Nhập b = "))
kq = 0

for i in range(pt):
    A.append(int(input("Nhập pt: ")))
    can = math.sqrt(A[i])

    if can >= a and can <= b:
        kq += 1

print(kq)