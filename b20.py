import math

pt = int(input("Nhập số phần tử có trong danh sách: "))

A = []

for i in range(pt):
    A.append(int(input("Nhập pt: ")))

x = int(input("Nhập x = "))

if x in A:
    print("Tìm thấy")

else:
    kcnn = 999
    gn = 0
    for i in range(pt):
        kc = abs(math.sqrt(A[i]) - x)
        if kc < kcnn:
            kcnn = kc
            gn = A[i]

    print("Gần nhất theo căn:", gn)