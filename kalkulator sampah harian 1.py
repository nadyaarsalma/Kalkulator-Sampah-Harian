from datetime import date

# Judul utama
st.set_page_config(page_title="Kalkulator Sampah Harian", layout="centered")

st.title("🌱 Kalkulator Sampah Harian")
st.subheader("Mencatat dan Mengurangi Sampah Dimulai dari Diri Sendiri")

# Tanggal hari ini
today = date.today()
st.markdown(f"📅 Tanggal hari ini: *{today.strftime('%d %B %Y')}*")

# Penjelasan singkat aplikasi
st.markdown("""
Aplikasi ini membantumu mencatat jumlah sampah yang kamu hasilkan setiap hari berdasarkan jenisnya:
- 🥦 Sampah Organik  
- 🧴 Sampah Anorganik (Plastik, Kertas, Logam, dll)  
- ☠ Sampah B3 (Bahan Berbahaya & Beracun)

Yuk mulai mencatat dan kurangi produksi sampah harianmu!  
""")
