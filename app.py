import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder, StandardScaler

model = pickle.load(open('model_knn.pkl', 'rb'))
print(model)
le = LabelEncoder()  # Inisialisasi LabelEncoder sekali
scaler = StandardScaler()  # Inisialisasi StandardScaler sekali

st.title('Estimasi Harga Mobil Bekas')

jenis = st.text_input('Input Model Mobil')
year = st.number_input('Input Tahun Mobil')
transmisi = st.text_input('Input Jenis Transmisi')
km = st.number_input('Input KM Mobil')
bahan_bakar = st.text_input('Input Bahan Bakar Mobil')
pajak = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
cc = st.number_input('Input Engine Size')

predict = ''

if st.button('Estimasi Harga'):
    # Encoding data kategorikal
    jenis_encoded = le.fit_transform([jenis])
    transmisi_encoded = le.fit_transform([transmisi])
    bahan_bakar_encoded = le.fit_transform([bahan_bakar])

    # Menggabungkan data input
    input_data = [jenis_encoded[0], year, transmisi_encoded[0], km, bahan_bakar_encoded[0], pajak, mpg, cc]

    # Scaling data input
    input_data_scaled = scaler.fit_transform([input_data])

    predict = model.predict(input_data_scaled)[0]
    st.write('Estimasi harga mobil IDR (juta) : ', predict)