import math

pt = int(input("Nhập số phần tử có trong danh sách: "))

A = []
Kq = []

for i in range(pt):
    A.append(int(input("Nhập pt: ")))
    can = math.sqrt(A[i])

    if can**2 != A[i]:
        continue

    j = can
    dx = 0
    while j > 0:
        dx = dx*10 + j % 10
        j //= 10

    if dx == can:
        Kq.append(can)

print(Kq)