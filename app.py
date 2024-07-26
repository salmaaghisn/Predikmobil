import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder, StandardScaler

model = pickle.load(open('model_knn.pkl', 'rb'))
print(model)
le = LabelEncoder()  # Inisialisasi LabelEncoder sekali
scaler = StandardScaler()  # Inisialisasi StandardScaler sekali

st.title('Estimasi Harga Mobil Bekas Toyota')
st.image("./img/image.png")
list_jenis = ['Agya', 'Calya', 'Avanza Veloz', 'Raize', 'Rush', 'Innova', 'Fortuner', 'Corolla Cross']
jenis = st.selectbox('Input Model Mobil', list_jenis)

year = st.text_input('Input Tahun Mobil')

list_transmisi = ['Matic', 'Manual']
transmisi = st.selectbox('Input Jenis Transmisi', list_transmisi)

km = st.text_input('Input KM Mobil')

list_bahan_bakar = ['Bensin', 'Diesel', 'Hybrid']
bahan_bakar = st.selectbox('Input Bahan Bakar Mobil', list_bahan_bakar)

pajak = st.text_input('Input Pajak Mobil')
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