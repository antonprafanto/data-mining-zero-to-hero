import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris, load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Fullstack Data Mining App",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Navigasi
st.sidebar.image("https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Python-Dark.svg", width=50)
st.sidebar.title("Data Mining Hub")
st.sidebar.markdown("Kurikulum **From Zero to Hero**")

menu = st.sidebar.radio(
    "Pilih Menu:",
    ["🏠 Beranda & Filosofi", "📊 Eksplorasi Data (EDA)", "🤖 Live Model Classifier", "🚀 Panduan Deployment Cloud"]
)

# ----------------- MENU 1: BERANDA -----------------
if menu == "🏠 Beranda & Filosofi":
    st.title("⛏️ Fullstack Data Mining: From Zero to Hero")
    st.markdown("""
    Selamat datang di **Aplikasi Interaktif Fullstack Data Mining**!  
    Aplikasi ini adalah bukti nyata bagaimana model data mining yang dilatih di **Google Colab** 
    dapat dikemas menjadi produk antarmuka pengguna berbasis web (*fullstack data application*).
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("### 1. Zero to Hero\nDirancang untuk pemula awam tanpa latar belakang rumit. Fokus pada intuisi nyata.")
    with col2:
        st.success("### 2. Google Colab Ready\n100% komputasi awan gratis tanpa instalasi lokal yang memusingkan.")
    with col3:
        st.warning("### 3. Fullstack Mindset\nTidak berhenti di notebook, tapi dideploy langsung menjadi web app interaktif.")

    st.markdown("---")
    st.subheader("🧭 Alur CRISP-DM di Balik Layar")
    st.markdown("""
    1. **Business Understanding**: Mengetahui tujuan dan masalah bisnis.
    2. **Data Understanding**: Memeriksa bentuk, sebaran, dan tipe variabel data.
    3. **Data Preparation**: Membersihkan nilai kosong (*missing values*) dan penskalaan (*scaling*).
    4. **Modeling**: Melatih algoritma machine learning (Supervised & Unsupervised).
    5. **Evaluation**: Menguji akurasi, presisi, recall, dan metrik lainnya.
    6. **Deployment**: Menyajikan model interaktif dalam bentuk aplikasi web ini!
    """)

# ----------------- MENU 2: EDA -----------------
elif menu == "📊 Eksplorasi Data (EDA)":
    st.title("📊 Eksplorasi Data Interaktif (EDA)")
    st.write("Eksplorasi dataset bawaan atau unggah file CSV Anda sendiri untuk melihat ringkasan statistik.")

    dataset_choice = st.selectbox("Pilih Dataset Contoh atau Upload Sendiri:", ["Iris Flowers (Bunga)", "Wine Quality (Anggur)", "Upload File CSV Sendiri"])

    if dataset_choice == "Iris Flowers (Bunga)":
        data_raw = load_iris(as_frame=True)
        df = data_raw.frame
    elif dataset_choice == "Wine Quality (Anggur)":
        data_raw = load_wine(as_frame=True)
        df = data_raw.frame
    else:
        uploaded_file = st.file_uploader("Unggah file CSV Anda", type=["csv"])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
        else:
            st.info("Silakan unggah file CSV terlebih dahulu.")
            df = None

    if df is not None:
        st.subheader("Pratinjau Data (5 Baris Teratas)")
        st.dataframe(df.head(), use_container_width=True)

        col_a, col_b = st.columns(2)
        with col_a:
            st.write(f"**Dimensi Data:** {df.shape[0]} baris × {df.shape[1]} kolom")
            st.write(f"**Nilai Kosong (Missing Values):** {df.isna().sum().sum()} sel")
        with col_b:
            st.write("**Tipe Data Kolom:**")
            st.dataframe(df.dtypes.astype(str).rename("Data Type"), use_container_width=True)

        st.subheader("Ringkasan Statistik Numerik")
        st.dataframe(df.describe().T, use_container_width=True)

        # Heatmap Korelasi
        numeric_df = df.select_dtypes(include=[np.number])
        if numeric_df.shape[1] > 1:
            st.subheader("🔥 Heatmap Korelasi Antar Fitur")
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
            st.pyplot(fig)

# ----------------- MENU 3: LIVE CLASSIFIER -----------------
elif menu == "🤖 Live Model Classifier":
    st.title("🤖 Live Model Classifier: Prediksi Real-Time")
    st.write("Uji coba model klasifikasi *Random Forest* secara interaktif. Ubah parameter input dan lihat hasil prediksinya secara instan!")

    # Load dataset Iris sebagai contoh interaktif
    data_raw = load_iris(as_frame=True)
    X = data_raw.data
    y = data_raw.target
    target_names = data_raw.target_names

    # Split & Train
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    st.success(f"Model berhasil dilatih pada data latih! Akurasi Data Uji: **{acc * 100:.1f}%**")

    st.subheader("Masukkan Parameter Fitur:")
    col1, col2 = st.columns(2)
    with col1:
        sepal_length = st.slider("Panjang Sepal (cm)", float(X['sepal length (cm)'].min()), float(X['sepal length (cm)'].max()), 5.4)
        sepal_width = st.slider("Lebar Sepal (cm)", float(X['sepal width (cm)'].min()), float(X['sepal width (cm)'].max()), 3.4)
    with col2:
        petal_length = st.slider("Panjang Petal (cm)", float(X['petal length (cm)'].min()), float(X['petal length (cm)'].max()), 1.5)
        petal_width = st.slider("Lebar Petal (cm)", float(X['petal width (cm)'].min()), float(X['petal width (cm)'].max()), 0.2)

    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    if st.button("🔮 Prediksi Sekarang", type="primary"):
        pred_class_idx = model.predict(input_data)[0]
        pred_proba = model.predict_proba(input_data)[0]
        pred_label = target_names[pred_class_idx]

        st.markdown(f"### Hasil Prediksi: **{pred_label.capitalize()}** 🌸")
        st.write(f"Tingkat Keyakinan (*Confidence*): **{pred_proba[pred_class_idx]*100:.2f}%**")

        # Tampilkan distribusi probabilitas
        proba_df = pd.DataFrame({
            "Spesies": [name.capitalize() for name in target_names],
            "Probabilitas": [f"{p*100:.1f}%" for p in pred_proba]
        })
        st.table(proba_df)

# ----------------- MENU 4: DEPLOYMENT GUIDE -----------------
elif menu == "🚀 Panduan Deployment Cloud":
    st.title("🚀 Cara Mendeploy Web App ke Streamlit Community Cloud (Gratis)")
    st.markdown("""
    Setelah Anda melatih model di Google Colab dan menyimpannya (`.joblib`), Anda dapat mempublikasikan web app ini ke internet secara **100% Gratis**!

    ### Langkah-Langkah:
    1. **Push Proyek ke GitHub**: Pastikan repository Anda berisi file `app/app.py` dan `requirements.txt`.
    2. **Kunjungi Streamlit Community Cloud**: Buka [share.streamlit.io](https://share.streamlit.io/) dan login menggunakan akun GitHub Anda.
    3. **Buat Aplikasi Baru**:
       - Klik tombol **"New app"**.
       - Pilih repositori: `antonprafanto/data-mining-zero-to-hero`.
       - Tentukan branch: `main`.
       - Masukkan Main file path: `app/app.py`.
    4. **Klik Deploy**: Tunggu 1–2 menit, dan aplikasi Anda sudah online dengan URL publik (contoh: `https://data-mining-zero-to-hero.streamlit.app`)!

    🎉 **Cantumkan URL tersebut di CV, LinkedIn, dan portofolio Anda!**
    """)

st.sidebar.markdown("---")
st.sidebar.caption("© 2026 Anton Prafanto - Data Mining Zero to Hero")
