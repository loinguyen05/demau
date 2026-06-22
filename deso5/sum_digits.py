n = int(input("Nhap so nguyen duong: "))

tong = 0
temp = n

while temp > 0:
    tong += temp % 10
    temp //= 10

print("Tong cac chu so la:", tong)