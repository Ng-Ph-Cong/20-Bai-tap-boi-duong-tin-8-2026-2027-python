import math

pt = int(input("Nhập số phần tử có trong danh sách: "))

A = []
kcnn = 999
soOne = 0
soTwo = 0

for i in range(pt):
    A.append(int(input("Nhập phần tử: ")))

if pt > 2:
    for i in range(0, pt):
        for j in range(i + 1, pt):
            kc = abs(math.sqrt(A[i]) - math.sqrt(A[j]))
            if kc < kcnn:
                kcnn = kc
                soOne = A[i]
                soTwo = A[j]

    print("Khoảng cách nhỏ nhất:", soOne, "và", soTwo)
elif pt == 2:
    print("Chỉ có một cặp")
elif pt < 2:
    print("Không thể so sánh")
