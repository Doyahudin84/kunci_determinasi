
import streamlit as st

# Judul aplikasi
st.title("Kunci Determinasi Tumbuhan - Aranademi")

# Penjelasan aplikasi
st.write("""
    Aplikasi ini membantu Anda dalam mencari nama tumbuhan berdasarkan kunci determinasi. 
    Pilihlah ciri-ciri tumbuhan sesuai dengan petunjuk pada setiap tingkat untuk menemukan jenis tumbuhan.
    -Aranademi-
""")

# Definisikan ciri-ciri untuk setiap tingkat
tingkat_1 = st.selectbox("1. Apakah tumbuhan berdaun lebar atau sempit?",
                         ["Daun lebar", "Daun sempit"])

tingkat_2 = None
tingkat_3 = None

# Berdasarkan pilihan tingkat pertama, tampilkan pilihan untuk tingkat kedua
if tingkat_1 == "Daun lebar":
    tingkat_2 = st.selectbox("2. Apakah tumbuhan memiliki bunga berwarna cerah?",
                             ["Ya", "Tidak"])
elif tingkat_1 == "Daun sempit":
    tingkat_2 = st.selectbox("2. Apakah tumbuhan memiliki batang tegak?",
                             ["Ya", "Tidak"])

# Berdasarkan pilihan tingkat kedua, tampilkan pilihan untuk tingkat ketiga
if tingkat_2 == "Ya":
    tingkat_3 = st.selectbox("3. Apakah tumbuhan memiliki duri di batang?",
                             ["Ya", "Tidak"])
elif tingkat_2 == "Tidak":
    tingkat_3 = st.selectbox("3. Apakah tumbuhan tumbuh tinggi?",
                             ["Ya", "Tidak"])

# Menentukan hasil berdasarkan pilihan
if tingkat_1 == "Daun lebar" and tingkat_2 == "Ya" and tingkat_3 == "Tidak":
    st.write("Tumbuhan yang Anda pilih adalah **Bunga Matahari**.")
elif tingkat_1 == "Daun lebar" and tingkat_2 == "Tidak" and tingkat_3 == "Ya":
    st.write("Tumbuhan yang Anda pilih adalah **Kaktus**.")
elif tingkat_1 == "Daun sempit" and tingkat_2 == "Ya" and tingkat_3 == "Tidak":
    st.write("Tumbuhan yang Anda pilih adalah **Lili**.")
elif tingkat_1 == "Daun sempit" and tingkat_2 == "Tidak" and tingkat_3 == "Ya":
    st.write("Tumbuhan yang Anda pilih adalah **Pohon Cemara**.")
else:
    st.write("Tumbuhan tidak ditemukan dalam kategori ini. Coba lagi dengan pilihan yang berbeda.")


