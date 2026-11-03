pt = int(input("Nhập số phần tử có trong danh sách: "))

A = []

for i in range(pt):
    A.append(int(input("Nhập phần tử: ")))

x = int(input("Nhập x = "))

if x in A:
    vtr = A.index(x) + 1
    print("vị trí", vtr)
else:
    print("Ko tìm thấy")