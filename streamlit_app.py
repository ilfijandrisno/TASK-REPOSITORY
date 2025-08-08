import streamlit as st
from datetime import date

st.set_page_config(page_title="Zeller’s Congruence", page_icon="📅")

st.title("🗓️ Penentu Hari dengan Zeller’s Congruence")

# Input widgets
tanggal = st.number_input("Tanggal", min_value=1, max_value=31, value=None,
                          placeholder="Masukkan tanggal (1-31)")
bulan   = st.number_input("Bulan",   min_value=1, max_value=12, value=None,
                          placeholder="Masukkan bulan (1-12)")
tahun   = st.number_input("Tahun",   min_value=1000, max_value=9999, value=None,
                          placeholder="Masukkan tahun (>=1000)")

# Zeller’s Congruence
def zeller(d, m, y):
    if m <= 2:
        m += 12
        y -= 1
    K, J = y % 100, y // 100
    h = (d + ((13*(m+1))//5) + K + (K//4) + (J//4) - 2*J) % 7
    hari = ["Sabtu", "Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat"][h]
    return hari

if st.button("Hitung Hari", disabled=any(v is None for v in (tanggal, bulan, tahun))):
    hari = zeller(tanggal, bulan, tahun)
    leap = "kabisat" if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0) else "bukan kabisat"
    st.success(f"Tahun {tahun} adalah tahun **{leap}**.")
    st.info(f"📅 {tanggal}-{bulan}-{tahun} jatuh pada hari **{hari}**")