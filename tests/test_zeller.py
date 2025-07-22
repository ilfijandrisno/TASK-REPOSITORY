from myapp.zeller import zeller_congruence, is_leap_year

def test_zeller():
    assert zeller_congruence(17, 8, 1945) == "Jumat"

def test_leap_year():
    assert is_leap_year(2024) == True
    assert is_leap_year(2025) == False
