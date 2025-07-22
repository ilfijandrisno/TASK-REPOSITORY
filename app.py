from myapp.zeller import zeller_congruence, is_leap_year
from myapp.utils import validate_full_date, get_valid_day, get_valid_month, get_valid_year

if __name__ == "__main__":
    #print("🔍 Cek Hari Menggunakan Zeller's Congruence")

    while True:
        day = get_valid_day()
        month = get_valid_month()
        year = get_valid_year()

        if is_leap_year(year):
            print(f"\nTahun {year} adalah tahun kabisat.")
        else:
            print(f"\nTahun {year} bukan tahun kabisat.")

        if validate_full_date(day, month, year):
            break
        else:
            # Deteksi kasus spesial: 29 Februari tapi bukan tahun kabisat
            if day == 29 and month == 2 and not is_leap_year(year):
                print(f"Kombinasi tidak valid: Tahun {year} bukan tahun kabisat, jadi tidak ada 29 Februari.\n")
            else:
                print(f"Kombinasi tanggal {day}-{month}-{year} tidak valid. Coba lagi!\n")

    hasil = zeller_congruence(day, month, year)
    print(f"\n📅 {day}-{month}-{year} jatuh pada hari **{hasil}**\n")
