import math

pt = int(input("Nhập số phần tử có trong danh sách: "))

A = []
A_sqrt = []

for i in range(pt):
    A.append(int(input("Nhap phan tu: ")))
    A_sqrt.append(round(math.sqrt(A[i]) * 1000) / 1000)

print(A_sqrt)