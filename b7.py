import math

pt = int(input("Nhập số phần tử có trong danh sách: "))

A = []
B = []

for i in range(pt):
    A.append(int(input("Nhập phần tử: ")))
    B.append(round(math.sqrt(A[i]) * 1000) / 1000)

x = float(input("nhập x = "))

if x in B :
    vtr = B.index(x)
    print("Tìm thấy tại vị trí", vtr+1)
else:
    print("Không tìm thấy")