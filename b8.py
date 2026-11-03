pt = int(input("Nhập số phần tử: "))

A = []
for i in range(pt):
    A.append(int(input("Nhập phần tử: ")))

x = int(input("Nhập x = "))

kcnn = 999
gn = 0

for i in range(pt):
    kc = abs(A[i] - x)
    if kc < kcnn:
        kcnn = kc
        gn = A[i]

print("gần nhất:", gn)