import math

pt = int(input("Nhập số phần tử có trong danh sách: "))

A = []
D = []

for i in range(pt):
    A.append(int(input("Nhập phần tử: ")))
    D.append(math.floor(math.sqrt(A[i])))

print(D)