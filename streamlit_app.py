import streamlit as st
col1, col2, col3 = st.columns([1, 3, 1])
# Judul Aplikasi
with col2:
    st.image('aranademi.png', width=300)
st.title("Kunci Determinasi Tumbuhan")

# Deskripsi aplikasi
st.write(
    """
    Aplikasi ini membantu mengidentifikasi jenis ikan berdasarkan ciri-ciri fisiknya.
    Ikuti langkah-langkah di bawah ini untuk mengetahui jenis ikan yang Anda amati.
    """
)

# Langkah pertama
st.subheader("1. Apakah tumbuhan memiliki klorofil dan dapat fotosintesis?")
tumbuhan_klorofil = st.radio("Pilih salah satu:", ('Tidak memiliki klorofil dan tidak dapat fotosintesis', 'Memiliki klorofil dan dapat fotosintesis'))

if tumbuhan_klorofil == 'Tidak memiliki klorofil dan tidak dapat fotosintesis':
    st.write("Identifikasi: **Jamur**")
elif tumbuhan_klorofil == 'Memiliki klorofil dan dapat fotosintesis':
    # Langkah kedua
    st.subheader("2. Apakah tumbuhan tersebut menghasilkan biji?")
    menghasilkan_biji = st.radio("Pilih salah satu:", ('Tidak menghasilkan biji', 'Menghasilkan biji'))

    if menghasilkan_biji == 'Tidak menghasilkan biji':
        st.write("Identifikasi: **Lumut**")
    elif menghasilkan_biji == 'Menghasilkan biji':
        # Langkah ketiga
        st.subheader("3. Apakah biji tumbuhan terbuka atau tertutup?")
        biji_terbuka_tertutup = st.radio("Pilih salah satu:", ('Biji terbuka, tidak memiliki bunga, sering berbentuk konus atau kerucut', 'Biji tertutup dalam buah'))

        if biji_terbuka_tertutup == 'Biji terbuka, tidak memiliki bunga, sering berbentuk konus atau kerucut':
            st.write("Identifikasi: **Gymnospermae**")
        elif biji_terbuka_tertutup == 'Biji tertutup dalam buah':
            # Langkah keempat
            st.subheader("4. Apakah tumbuhan memiliki daun dengan satu kotiledon atau dua kotiledon?")
            kotiledon = st.radio("Pilih salah satu:", ('Daun dengan urat sejajar, memiliki satu kotiledon', 'Daun dengan urat bersirip, memiliki dua kotiledon'))

            if kotiledon == 'Daun dengan urat sejajar, memiliki satu kotiledon':
                st.write("Identifikasi: **Monokotil**")
            elif kotiledon == 'Daun dengan urat bersirip, memiliki dua kotiledon':
                st.write("Identifikasi: **Dikotil**")
