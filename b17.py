import math

pt = int(input("Nhập số phần tử có trong danh sách: "))

A = []
gn = 0
kcnn = 999

for i in range(pt):
    A.append(int(input("Nhập pt: ")))

if pt > 1:
    TBC = float(input("Nhập trung bình căn: "))
    for i in range(pt):
        kc = abs(math.sqrt(A[i]) - TBC)
        if kc < kcnn:
            kcnn = kc
            gn = A[i]

    print("Gần nhất:", gn)

elif pt == 1:
    print("Chính nó")