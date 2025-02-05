import streamlit as st
col1, col2, col3 = st.columns([1, 3, 1])
# Judul Aplikasi
with col2
    st.image('aranademi.png', width=200)
st.title("Kunci Determinasi Jenis Ikan")

# Deskripsi aplikasi
st.write(
    """
    Aplikasi ini membantu mengidentifikasi jenis ikan berdasarkan ciri-ciri fisiknya.
    Ikuti langkah-langkah di bawah ini untuk mengetahui jenis ikan yang Anda amati.
    """
)

# Fungsi untuk menentukan jenis ikan berdasarkan input
def identifikasi_ikan(sirip_punggung, tubuh, sirip_panjang, mulut_besar, habitat):
    if sirip_punggung == "Ganda":
        return "Ikan Kerapu"
    elif tubuh == "Ramping dan panjang":
        if sirip_panjang == "Panjang dan torpedo":
            return "Ikan Tuna"
        else:
            return "Ikan Tenggiri"
    elif mulut_besar == "Ya":
        return "Ikan Hiu"
    elif habitat == "Dasar perairan atau terumbu karang":
        return "Ikan Kakap"
    else:
        return "Ikan Nila"

# Input pengguna
sirip_punggung = st.selectbox(
    "Apakah ikan memiliki sirip punggung ganda atau tunggal?",
    ["Tunggal", "Ganda"]
)

tubuh = st.selectbox(
    "Apakah ikan memiliki tubuh ramping dan panjang?",
    ["Ramping dan panjang", "Gemuk atau bulat"]
)

sirip_panjang = st.selectbox(
    "Apakah sirip punggung ikan panjang dan tubuhnya seperti torpedo?",
    ["Panjang dan torpedo", "Tidak"]
)

mulut_besar = st.selectbox(
    "Apakah ikan memiliki mulut besar dengan gigi tajam?",
    ["Ya", "Tidak"]
)

habitat = st.selectbox(
    "Apakah ikan sering ditemukan di dasar perairan atau terumbu karang?",
    ["Dasar perairan atau terumbu karang", "Perairan terbuka"]
)

# Tombol untuk menampilkan hasil
if st.button("Identifikasi Jenis Ikan"):
    hasil = identifikasi_ikan(sirip_punggung, tubuh, sirip_panjang, mulut_besar, habitat)
    st.write(f"Jenis ikan yang Anda identifikasi adalah: **{hasil}**")


