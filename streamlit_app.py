import streamlit as st
from datetime import date
import calendar

# -----------------------------
#  Metadata & Kredit
# -----------------------------
APP_NAME = "🗓️ Penentu Hari dengan Zeller’s Congruence"
AUTHOR   = "Ilfi Jandrisno"
GITHUB   = "https://github.com/ilfijandrisno/TASK-REPOSITORY"

st.set_page_config(
    page_title=APP_NAME,
    page_icon="📅",
    layout="centered"
)

st.title(APP_NAME)

# -----------------------------
#  Input form
# -----------------------------
tanggal = st.number_input("Tanggal", min_value=1, max_value=31, value=None,
                          placeholder="Masukkan tanggal (1-31)")
bulan   = st.number_input("Bulan", min_value=1, max_value=12, value=None,
                          placeholder="Masukkan bulan (1-12)")
tahun   = st.number_input("Tahun", min_value=1000, max_value=9999, value=None,
                          placeholder="Masukkan tahun (>=1000)")

# -----------------------------
#  Zeller’s Congruence
# -----------------------------
def zeller(d, m, y):
    if m <= 2:
        m += 12
        y -= 1
    K, J = y % 100, y // 100
    h = (d + ((13*(m+1))//5) + K + (K//4) + (J//4) - 2*J) % 7
    return ["Sabtu", "Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat"][h]

# -----------------------------
#  Hasil
# -----------------------------
if st.button("Hitung Hari", disabled=any(v is None for v in (tanggal, bulan, tahun))):
    try:
        # validasi & normalisasi
        dt = date(tahun, bulan, tanggal)
    except ValueError as e:
        st.error(f"⚠️ {e}")
        # --- penjelasan & solusi ---
        with st.expander("💡 Penjelasan & tanggal yang benar"):
            days_in_month = calendar.monthrange(tahun, bulan)[1]
            st.write(
                f"Bulan **{calendar.month_name[bulan]} {tahun}** hanya memiliki **{days_in_month} hari**. "
                f"Gunakan tanggal **1 – {days_in_month}**."
            )
        st.stop()     
    hari = zeller(tanggal, bulan, tahun)
    leap = "kabisat" if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0) else "bukan kabisat"
    st.success(f"Tahun {tahun} adalah tahun **{leap}**.")
    st.info(f"📅 {tanggal}-{bulan}-{tahun} jatuh pada hari **{hari}**")

# -----------------------------
#  Footer
# -----------------------------
st.divider()
st.markdown(
    f"""
    <div style='text-align: center; font-size: 0.9em; color: #888;'>
        © 2024 <a href='{GITHUB}' target='_blank'>{AUTHOR}</a> — All rights reserved.
    </div>
    """,
    unsafe_allow_html=True
)