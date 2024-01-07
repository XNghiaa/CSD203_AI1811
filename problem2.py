def problem2(diem):
    if 8.5 <= diem <= 10:
        return 'A'
    elif 7.0 <= diem < 8.5:
        return 'B'
    elif 5.5 <= diem < 7:
        return "C"
    elif 4.0 <= diem < 5.5:
        return "D"
    else:
        return "F"
def chuyen_doi_he_4(diem):
    if diem >= 9.0:
        return '4.0'
    elif diem >= 8.5:
        return '4.0'
    elif diem >= 8.0:
        return '3.7'
    elif diem >= 7.0:
        return '3.3'
    elif diem >= 6.5:
        return '3.0'
    elif diem >= 5.5:
        return '2.7'
    elif diem >= 5.0:
        return '2.3'
    elif diem >= 4.0:
        return '2.0'
    else:
        return '0.0'

def main():
    try:
        diem = float(input("Nhập điểm theo hệ thập phân: "))
        
        if 0.0 <= diem <= 10.0:
            diem_chu_cai = problem2(diem)
            diem_he_4 = chuyen_doi_he_4(diem)

            print(f"Điểm chữ cái tương ứng: {diem_chu_cai}")
            print(f"Điểm theo hệ 4 tương ứng: {diem_he_4}")
        else:
            print("Điểm không hợp lệ! Hãy nhập điểm trong khoảng từ 0 đến 10.")
    except ValueError:
        print("Dữ liệu nhập không hợp lệ! Hãy nhập một số thập phân hợp lệ.")

if __name__ == "__main__":
    main()
