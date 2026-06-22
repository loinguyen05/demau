n = int(input("Nhap n: "))

factorial = 1

if n < 0:
    print("Khong tinh duoc giai thua cua so am")
else:
    for i in range(1, n + 1):
        factorial *= i

    print(f"Giai thua cua {n} la: {factorial}")