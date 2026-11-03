pt = int(input("Nhập số phần tử có trong danh sách: "))

A = []
Kq = []

for i in range(pt):
    A.append(int(input("Nhập phần tử: ")))

x = int(input("nhập x = "))

for i in range(pt):
    if A[i] > x:
        Kq.append(A[i])

print(Kq)