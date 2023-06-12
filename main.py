import streamlit as st 
import pandas as pd
from PIL import Image
import pickle

im = Image.open('src/public/Arahku-removebg-preview.png')

st.set_page_config(page_title="MBIT",page_icon = im)
st.image('src/public/Arahku-removebg-preview.png')

st.write("""
    # Sistem Penentuan Jurusan Sesuai Minat Bakat
""")

# get user input from web
soal1 = st.selectbox('Saya memiliki kemampuan matematika dan analitis yang tinggi', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal2 = st.selectbox('Saya lebih condong ke arah penelitian artistik', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal3 = st.selectbox('Saya menikmati pembelajran dengan teknologi dan komputer', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal4 = st.selectbox('Saya tertarik dalam memahami perilaku dan motivasi manusia', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal5 = st.selectbox('Saya tertarik dalam memecahkan masalah teknis maupun ilmiah', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal6 = st.selectbox('Saya memiliki kecenderungan kuat dalam ekspresi kreatif', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal7 = st.selectbox('Saya tertarik untuk menjelajahi budaya dan perspektif yang berbeda', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal8 = st.selectbox('Penting bagi saya untuk memberikan dampak positif pada kehidupan orang lain', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal9 = st.selectbox('Saya lebih condong pada pengetahuan praktis maupun teoritis', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal10 = st.selectbox('Saya nyaman dalam melakukan perbicara di depan umum dan melakukan presentasi', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal11 = st.selectbox('Saya tertarik pada masalah lingkungan dan pelestarian alam', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal12 = st.selectbox('Saya mahir Anda dalam berpikir kritis dan pemecahan masalah', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal13 = st.selectbox('Saya sangat menikmati melakukan percobaan dan menganalisis data', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal14 = st.selectbox('Saya tertarik dalam mempelajari bisnis dan kewirausahaan', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal15 = st.selectbox('Saya tertarik bekerja dalam tim dan berkolaborasi dengan orang lain ?', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal16 = st.selectbox('Saya tertarik dalam bidang kesehatan dan medis ?', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal17 = st.selectbox('Saya sangat menyykai kreativitas dan inovasi', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal18 = st.selectbox('Saya memiliki minat yang kuat dalam sastra dan bahasa', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal19 = st.selectbox('Saya cenderung suka pada penelitian dan kegiatan akademik', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
soal20 = st.selectbox('Saya tertarik dalam memahami ilmu sosial dan pemahaman masyarakat', ('Sangat Tidak Setuju', 'Tidak Setuju','Netral','Setuju', 'Sangat Setuju'))
reveal = st.button('Tampilkan Hasil')

# create new data from user input and convert value to float
new_data = {
    # If value = "Setuju" then convert to 0.0, else convert to 0
    'soal1': 0.0 if soal1 == 'Sangat Tidakk Setuju' else 1.0 if soal1 == 'Tidakk Setuju' else 2.0 if soal1 == 'Netral' else 3.0 if soal1 == 'Setuju' else 4.0,
    'soal2': 0.0 if soal2 == 'Sangat Tidakk Setuju' else 1.0 if soal2 == 'Tidakk Setuju' else 2.0 if soal2 == 'Netral' else 3.0 if soal2 == 'Setuju' else 4.0,
    'soal3': 0.0 if soal3 == 'Sangat Tidakk Setuju' else 1.0 if soal3 == 'Tidakk Setuju' else 2.0 if soal3 == 'Netral' else 3.0 if soal3 == 'Setuju' else 4.0,
    'soal4': 0.0 if soal4 == 'Sangat Tidakk Setuju' else 1.0 if soal4 == 'Tidakk Setuju' else 2.0 if soal4 == 'Netral' else 3.0 if soal4 == 'Setuju' else 4.0,
    'soal5': 0.0 if soal5 == 'Sangat Tidakk Setuju' else 1.0 if soal5 == 'Tidakk Setuju' else 2.0 if soal5 == 'Netral' else 3.0 if soal5 == 'Setuju' else 4.0,
    'soal6': 0.0 if soal6 == 'Sangat Tidakk Setuju' else 1.0 if soal6 == 'Tidakk Setuju' else 2.0 if soal6 == 'Netral' else 3.0 if soal6 == 'Setuju' else 4.0,
    'soal7': 0.0 if soal7 == 'Sangat Tidakk Setuju' else 1.0 if soal7 == 'Tidakk Setuju' else 2.0 if soal7 == 'Netral' else 3.0 if soal7 == 'Setuju' else 4.0,
    'soal8': 0.0 if soal8 == 'Sangat Tidakk Setuju' else 1.0 if soal8 == 'Tidakk Setuju' else 2.0 if soal8 == 'Netral' else 3.0 if soal8 == 'Setuju' else 4.0,
    'soal9': 0.0 if soal9 == 'Sangat Tidakk Setuju' else 1.0 if soal9 == 'Tidakk Setuju' else 2.0 if soal9 == 'Netral' else 3.0 if soal9 == 'Setuju' else 4.0,
    'soal10': 0.0 if soal10 == 'Sangat Tidakk Setuju' else 1.0 if soal10 == 'Tidakk Setuju' else 2.0 if soal10 == 'Netral' else 3.0 if soal10 == 'Setuju' else 4.0,
    'soal11': 0.0 if soal11 == 'Sangat Tidakk Setuju' else 1.0 if soal11 == 'Tidakk Setuju' else 2.0 if soal11 == 'Netral' else 3.0 if soal11 == 'Setuju' else 4.0,
    'soal12': 0.0 if soal12 == 'Sangat Tidakk Setuju' else 1.0 if soal12 == 'Tidakk Setuju' else 2.0 if soal12 == 'Netral' else 3.0 if soal12 == 'Setuju' else 4.0,
    'soal13': 0.0 if soal13 == 'Sangat Tidakk Setuju' else 1.0 if soal13 == 'Tidakk Setuju' else 2.0 if soal13 == 'Netral' else 3.0 if soal13 == 'Setuju' else 4.0,
    'soal14': 0.0 if soal14 == 'Sangat Tidakk Setuju' else 1.0 if soal14 == 'Tidakk Setuju' else 2.0 if soal14 == 'Netral' else 3.0 if soal14 == 'Setuju' else 4.0,
    'soal15': 0.0 if soal15 == 'Sangat Tidakk Setuju' else 1.0 if soal15 == 'Tidakk Setuju' else 2.0 if soal15 == 'Netral' else 3.0 if soal15 == 'Setuju' else 4.0,
    'soal16': 0.0 if soal16 == 'Sangat Tidakk Setuju' else 1.0 if soal16 == 'Tidakk Setuju' else 2.0 if soal16 == 'Netral' else 3.0 if soal16 == 'Setuju' else 4.0,
    'soal17': 0.0 if soal17 == 'Sangat Tidakk Setuju' else 1.0 if soal17 == 'Tidakk Setuju' else 2.0 if soal17 == 'Netral' else 3.0 if soal17 == 'Setuju' else 4.0,
    'soal18': 0.0 if soal18 == 'Sangat Tidakk Setuju' else 1.0 if soal18 == 'Tidakk Setuju' else 2.0 if soal18 == 'Netral' else 3.0 if soal18 == 'Setuju' else 4.0,
    'soal19': 0.0 if soal19 == 'Sangat Tidakk Setuju' else 1.0 if soal19 == 'Tidakk Setuju' else 2.0 if soal19 == 'Netral' else 3.0 if soal19 == 'Setuju' else 4.0,
    'soal20': 0.0 if soal20 == 'Sangat Tidakk Setuju' else 1.0 if soal20 == 'Tidakk Setuju' else 2.0 if soal20 == 'Netral' else 3.0 if soal20 == 'Setuju' else 4.0,
}


# create new dataframe from new data
new_df = pd.DataFrame(new_data, index=[0])

# load model
model = pickle.load(open('Model/model.pkl', 'rb'))

# predict new data with button but if all value is 0.0 then show error
if reveal:
    # check if soal1 until soal15 is 0.0
    if new_df['soal1'].values[0] == 1.0 and new_df['soal2'].values[0] == 1.0 and new_df['soal3'].values[0] == 1.0 and new_df['soal4'].values[0] == 1.0 and new_df['soal5'].values[0] == 1.0 and new_df['soal6'].values[0] == 1.0 and new_df['soal7'].values[0] == 1.0 and new_df['soal8'].values[0] == 1.0 and new_df['soal9'].values[0] == 1.0 and new_df['soal10'].values[0] == 1.0 and new_df['soal11'].values[0] == 1.0 and new_df['soal12'].values[0] == 1.0 and new_df['soal13'].values[0] == 1.0 and new_df['soal14'].values[0] == 1.0 and new_df['soal15'].values[0] == 1.0 and new_df['soal16'].values[0] == 1.0 and new_df['soal17'].values[0] == 1.0 and new_df['soal18'].values[0] == 1.0 and new_df['soal19'].values[0] == 1.0 and new_df['soal20'].values[0] == 1.0:
        st.write('Mohon pilih jawaban terlebih dahulu')
    else:
       prediction = model.predict(new_df)
       st.write('Jurusan yang sesuai dengan kamu : ', prediction[0])
