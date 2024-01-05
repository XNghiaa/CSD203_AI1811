def problem1(n):
    chuoi_n = str(n)
    
    cac_chu_so = [int(chu_so) for chu_so in chuoi_n]
    
    return cac_chu_so

n = int(input("Nhập số nguyên dương n (0 < n < 1000): "))

if 0 < n < 1000:
    ket_qua = problem1(n)
    print(f"Các chữ số của số {n} là: {ket_qua}")
else:
    print("Vui lòng nhập số nguyên dương n trong khoảng từ 1 đến 999.")
