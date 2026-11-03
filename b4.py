import math

pt = int(input("Nhập số phần tử có trong danh sách: "))

A = []
A_Sqrt = []
lon_nhat = 0

for i in range(pt):
    A.append(int(input("Nhập phần tử : ")))
    A_Sqrt.append(round(math.sqrt(A[i]) * 1000) / 1000)

    if A_Sqrt[i] > lon_nhat:
        lon_nhat = A_Sqrt[i]

vtr = A_Sqrt.index(lon_nhat)

print("Lớn nhất: ", A[vtr], ", vị trí: ", vtr+1)