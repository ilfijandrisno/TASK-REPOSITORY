import datetime

def get_valid_day():
    while True:
        try:
            day = int(input("Masukkan tanggal (1–31): "))
            if 1 <= day <= 31:
                return day
            else:
                print("Tanggal harus antara 1 sampai 31!")
        except ValueError:
            print("Tanggal harus berupa angka!")

def get_valid_month():
    while True:
        try:
            month = int(input("Masukkan bulan (1–12): "))
            if 1 <= month <= 12:
                return month
            else:
                print("Bulan harus antara 1 sampai 12!")
        except ValueError:
            print("Bulan harus berupa angka!")

def get_valid_year():
    while True:
        try:
            year = int(input("Masukkan tahun (>= 1000): "))
            if year >= 1000:
                return year
            else:
                print("Tahun harus 4 digit (misalnya 1945, 2023, dst).")
        except ValueError:
            print("Tahun harus berupa angka!")

def validate_full_date(day, month, year):
    try:
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False