# TASK-REPOSITORY
## 🗓️ Program Penentu Hari dengan Zeller's Congruence

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python&logoColor=white)](https://www.python.org/) ![Status](https://img.shields.io/badge/status-stable-brightgreen) ![License](https://img.shields.io/badge/license-MIT-green)

---

Program ini dibuat untuk menentukan hari dalam seminggu berdasarkan input **tanggal**, **bulan**, dan **tahun** dari pengguna. Perhitungan dilakukan menggunakan **Zeller’s Congruence**, yaitu rumus matematika yang umum digunakan dalam sistem kalender modern.

---

### ✨ Fitur Utama
✅ Validasi input tanggal, bulan, dan tahun
✅ Deteksi tahun kabisat (leap year)
✅ Perhitungan hari yang akurat menggunakan Zeller's Congruence

---

### ❓ Kenapa Harus Menggunakan Program Ini?
Program ini cocok digunakan oleh siapa saja yang ingin:

🔹 **Mengetahui hari dari tanggal tertentu** dengan cepat dan akurat  
🔹 **Memahami logika penentuan hari** dalam seminggu secara matematis  
🔹 **Mendapat validasi otomatis** untuk tanggal yang tidak mungkin ada  
🔹 **Belajar Python** melalui contoh nyata dan mudah dimengerti  
🔹 **Menggunakan tool ringan & offline** yang bisa dijalankan di semua OS

---

### 🎯 Kapan Program Ini Berguna?
- Mengecek hari dari tanggal sejarah (misal: 17 Agustus 1945)
- Mengisi formulir atau dokumen yang butuh informasi hari dan tanggal
- Membuat aplikasi kalender atau perhitungan ulang hari otomatis
- Belajar konsep tahun kabisat dan validasi tanggal secara logis

---

### 📥 Contoh Input
```bash
Masukkan tanggal (1–31): 29
Masukkan bulan (1–12): 2
Masukkan tahun (>= 1000): 2025
ℹ️ Tahun 2025 bukan tahun kabisat.
❌ Kombinasi tidak valid: Tahun 2025 bukan tahun kabisat, jadi tidak ada 29 Februari.
```

### 📤 Contoh Output Valid
```bash
Masukkan tanggal (1–31): 17
Masukkan bulan (1–12): 8
Masukkan tahun (>= 1000): 1945
ℹ️ Tahun 1945 bukan tahun kabisat.

📅 17-8-1945 jatuh pada hari **Jumat**
```

### 📚 Penjelasan Singkat Zeller’s Congruence
Zeller’s Congruence adalah rumus yang digunakan untuk menghitung hari dalam minggu dari sebuah tanggal tertentu. Rumusnya memetakan tanggal menjadi angka antara 0–6, yang merepresentasikan:

| Nilai | Hari     |
|-------|----------|
| 0     | Sabtu    |
| 1     | Minggu   |
| 2     | Senin    |
| 3     | Selasa   |
| 4     | Rabu     |
| 5     | Kamis    |
| 6     | Jumat    |

📌 Januari dan Februari dihitung sebagai bulan ke-13 dan ke-14 dari tahun sebelumnya.

### 🛠 Cara Menjalankan
Pastikan kamu sudah punya Python terinstal. Jalankan di terminal:

1. Pastikan Python sudah terinstal
2. Clone repo ini:
```bash
git clone https://github.com/ilfijandrisno/TASK-REPOSITORY.git
cd nama-repo
```
3. Jalankan program:
```bash
python app.py
```