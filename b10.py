pt = int(input("Nhập số phần tử: "))

A = []
for i in range(pt):
    A.append(int(input("Nhập phần tử: ")))

nn = max(A)
vtr = A.index(nn) + 1

print("lớn nhất:", nn,"vị trí:", vtr)