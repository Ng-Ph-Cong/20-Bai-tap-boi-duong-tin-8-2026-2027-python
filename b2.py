import math

pt = int(input("Nhập số phần tử có trong danh sách: "))

A = []
kq = []
can = 0

for i in range(pt):
    A.append(int(input("Nhập phần tử: ")))
    can = round(math.sqrt(A[i]) * 1000 ) /1000
    if can * can == A[i]:
        kq.append(A[i])

if len(kq) > 0:
    print(kq)
else:
    print("Không có")