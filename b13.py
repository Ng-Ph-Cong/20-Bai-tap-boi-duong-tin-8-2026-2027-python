pt = int(input("Nhập số phần tử có trong danh sách: "))

A = []
Kq = []

for i in range(pt):
    A.append(int(input("Nhập phần tử: ")))
    if A[i] % 2 == 0 or A[i] == 0:
        Kq.append(0)
    else:
        Kq.append(1)

print(Kq)