pt = int(input("Nhập số pt có trong danh sách: "))

A = []
C = []

for i in range(pt):
    A.append(int(input("Nhập phần tử: ")))
    C.append(A[i] **2)

print(C)