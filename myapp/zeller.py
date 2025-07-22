def zeller_congruence(day, month, year):
    if month in [1, 2]:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    h = (day + ((13 * (month + 1)) // 5) + K + (K // 4) + (J // 4) + 5 * J) % 7
    days = ["Sabtu", "Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
    return days[h]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)