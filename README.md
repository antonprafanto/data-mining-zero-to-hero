# 🚀 Fullstack Data Mining: From Zero to Hero

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Google Colab](https://img.shields.io/badge/Google%20Colab-Ready-orange.svg?logo=googlecolab&logoColor=white)](https://colab.research.google.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-F7931E.svg?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Interactive%20App-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Panduan dan Kurikulum Lengkap Belajar Data Mining Berbasis Cloud (Google Colab)**  
> *Didesain khusus untuk pemula dan pembelajar awam yang ingin menguasai data mining dari dasar konseptual, implementasi algoritma, hingga mendeploy model menjadi aplikasi web interaktif (*Fullstack*).*

---

## 📖 Tentang Repositori Ini

Apakah Anda seorang pemula yang ingin belajar data mining tetapi:
- ❌ Takut dengan rumus matematika dan statistik yang rumit?
- ❌ Bingung mulai dari mana dan pusing instalasi environment Python di laptop?
- ❌ Merasa materi yang ada hanya berhenti di file notebook (`.ipynb`) tanpa tahu cara menggunakannya di dunia nyata?

**Repositori ini adalah solusinya!**  
Di sini, kita belajar dengan prinsip **"Intuisi Dahulu, Rumus Menyusul"**. Seluruh materi praktik dirancang untuk dijalankan di **Google Colab** (100% gratis di browser, tanpa membebani laptop), dan kita melangkah lebih jauh: **mengubah model data mining menjadi aplikasi web interaktif (Streamlit)** yang siap dibagikan ke publik dan dicantumkan di CV/portofolio Anda.

---

## 🗺️ Silabus & Navigasi Modul

Silabus lengkap dan mendalam dapat dibaca di dokumen [**SILABUS.md**](SILABUS.md).  
Panduan komitmen dan pengerjaan proyek akhir dapat dibaca di [**KONTRAK-DAN-PANDUAN-PROYEK.md**](KONTRAK-DAN-PANDUAN-PROYEK.md).

| Modul | Topik Pembelajaran | Fokus Utama | Tautan Colab |
| :---: | :--- | :--- | :---: |
| **00** | **Mindset Data Mining & Google Colab Onboarding** | Pengenalan KDD/CRISP-DM, antarmuka Colab, shortcut, cloud storage | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/00_Onboarding_Google_Colab.ipynb) |
| **01** | **Fondasi Python & Manipulasi Data Tabel** | Tipe data, List, Dict, Pandas DataFrame, NumPy, Visualisasi Matplotlib/Seaborn | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/01_Python_Pandas_Numpy_Basics.ipynb) |
| **02** | **Data Cleaning & Preprocessing (Jantung Data Mining)** | Penanganan Missing Values, Outliers (IQR/Z-Score), Scaling (MinMax/Standard), Categorical Encoding | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/02_Data_Cleaning_and_Preprocessing.ipynb) |
| **03** | **Exploratory Data Analysis (EDA) & Feature Engineering** | Analisis univariat/bivariat, korelasi heatmap, rekayasa fitur tanggal/rasio, seleksi fitur | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/03_EDA_and_Feature_Engineering.ipynb) |
| **04** | **Supervised Learning I: Klasifikasi (Classification)** | K-NN, Naive Bayes, Decision Tree, Random Forest, Confusion Matrix, Imbalanced Data (SMOTE) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/04_Classification_Algorithms.ipynb) |
| **05** | **Supervised Learning II: Regresi (Regression)** | Linear Regression, Polynomial, Random Forest Regressor, Evaluasi MAE, RMSE, R² | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/05_Regression_Algorithms.ipynb) |
| **06** | **Unsupervised Learning I: Klasterisasi (Clustering)** | K-Means (Elbow Method & Silhouette), Hierarchical (Dendrogram), DBSCAN, PCA Dimensionality Reduction | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/06_Clustering_and_PCA.ipynb) |
| **07** | **Unsupervised Learning II: Aturan Asosiasi (Association Rules)** | Market Basket Analysis, Algoritma Apriori & FP-Growth, Support, Confidence, Lift Ratio | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/07_Association_Rule_Mining.ipynb) |
| **08** | **Deteksi Anomali & Dasar Text Mining (NLP)** | Isolation Forest (Fraud Detection), Text Preprocessing, TF-IDF, Analisis Sentimen Ulasan | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/08_Anomaly_Detection_and_Text_Mining.ipynb) |
| **09** | **Hyperparameter Tuning, Pipeline & Serialisasi Model** | Cross-Validation, GridSearchCV, Scikit-Learn Pipeline, Export model `.joblib` | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/09_Pipeline_and_Model_Export.ipynb) |
| **10** | **The Fullstack Milestone: Web App Interaktif (Streamlit)** | Membangun UI Streamlit, load model `.joblib`, prediksi real-time & batch CSV, deploy ke Streamlit Cloud | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/10_Streamlit_Web_App_Colab.ipynb) |
| **11** | **Capstone Project Akhir & Portofolio Ready** | Proyek mandiri end-to-end dari data mentah hingga web app live + dokumentasi portofolio GitHub | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/11_Capstone_Project_Guide.ipynb) |

---

## 🔄 Metodologi CRISP-DM

Seluruh pembelajaran di repositori ini mengacu pada standar proses data mining industri internasional (**CRISP-DM**):

```
                   ┌──────────────────────────────┐
                   │    Business Understanding    │
                   └──────────────┬───────────────┘
                                  │
                                  ▼
                   ┌──────────────────────────────┐
            ┌─────►│      Data Understanding      │
            │      └──────────────┬───────────────┘
            │                     │
            │                     ▼
            │      ┌──────────────────────────────┐
            └──────┤       Data Preparation       │◄─────┐
                   └──────────────┬───────────────┘      │
                                  │                      │
                                  ▼                      │
                   ┌──────────────────────────────┐      │
                   │           Modeling           ├──────┘
                   └──────────────┬───────────────┘
                                  │
                                  ▼
                   ┌──────────────────────────────┐
                   │          Evaluation          │
                   └──────────────┬───────────────┘
                                  │
                                  ▼
                   ┌──────────────────────────────┐
                   │          Deployment          │ (Web App Live)
                   └──────────────────────────────┘
```

---

## 💻 Cara Menggunakan Repositori Ini

### Opsi A: Langsung Melalui Browser (Direkomendasikan via Google Colab)
1. Pilih modul yang ingin dipelajari dari tabel di atas.
2. Klik tombol **Open in Colab** untuk membuka notebook langsung di browser Anda.
3. Masuk (*Sign-in*) dengan akun Google Anda.
4. Klik **File -> Simpan salinan di Drive** (*Save a copy in Drive*) agar progres latihan Anda tersimpan di Google Drive pribadi.

### Opsi B: Menjalankan Secara Lokal di Komputer Anda
Jika Anda ingin menjalankan atau mengembangkan web app Streamlit di komputer lokal:

```bash
# 1. Clone repositori ini
git clone https://github.com/antonprafanto/data-mining-zero-to-hero.git

# 2. Masuk ke direktori repositori
cd data-mining-zero-to-hero

# 3. Buat dan aktifkan virtual environment (opsional tapi disarankan)
python -m venv venv
# Di Windows:
.\venv\Scripts\activate
# Di macOS / Linux:
source venv/bin/activate

# 4. Instal seluruh pustaka yang dibutuhkan
pip install -r requirements.txt

# 5. Jalankan aplikasi web Streamlit
streamlit run app/app.py
```

---

## 📁 Struktur Direktori Repositori

```plaintext
data-mining-zero-to-hero/
│
├── .gitignore                      # File pengecualian git
├── requirements.txt                # Daftar pustaka dependensi Python
├── README.md                       # Halaman utama repositori
├── SILABUS.md                      # Silabus kurikulum detail per-modul
├── KONTRAK-DAN-PANDUAN-PROYEK.md   # Pedoman komitmen belajar dan Capstone
│
├── notebooks/                      # File Jupyter Notebook Google Colab
│   ├── 00_Onboarding_Google_Colab.ipynb
│   ├── 01_Python_Pandas_Numpy_Basics.ipynb
│   ├── 02_Data_Cleaning_and_Preprocessing.ipynb
│   ├── 03_EDA_and_Feature_Engineering.ipynb
│   ├── 04_Classification_Algorithms.ipynb
│   ├── 05_Regression_Algorithms.ipynb
│   ├── 06_Clustering_and_PCA.ipynb
│   ├── 07_Association_Rule_Mining.ipynb
│   ├── 08_Anomaly_Detection_and_Text_Mining.ipynb
│   ├── 09_Pipeline_and_Model_Export.ipynb
│   ├── 10_Streamlit_Web_App_Colab.ipynb
│   └── 11_Capstone_Project_Guide.ipynb
│
├── datasets/                       # Sampel dataset latihan kecil & panduan sumber data
│   └── README.md
│
├── app/                            # Kode aplikasi web interaktif (Streamlit)
│   ├── app.py                      # Skrip utama web app
│   └── README.md                   # Petunjuk menjalankan & deploy web app
│
└── docs/                           # Dokumentasi pendukung dan ilustrasi diagram
```

---

## 🌟 Siapa yang Cocok Mengikuti Materi Ini?
- 🎓 **Mahasiswa / Pelajar**: Yang sedang mengambil mata kuliah Data Mining, Machine Learning, atau mempersiapkan skripsi berbasis data.
- 💼 **Profesional / Switch Career**: Yang ingin beralih profesi menjadi Data Analyst, Data Scientist, atau AI/ML Engineer.
- 🧑‍💻 **Pembelajar Mandiri (Autodidak)**: Yang ingin memahami sains data secara terstruktur tanpa tersesat di tumpukan tutorial acak di internet.

---

## 🤝 Kontribusi & Dukungan
Kontribusi dalam bentuk *pull request*, pelaporan *issue*, saran materi, atau perbaikan *typo* sangat disambut dengan hangat!
Jika repositori ini bermanfaat bagi perjalanan belajar Anda, jangan lupa berikan **Star ⭐** di GitHub!

---

## 📜 Lisensi
Proyek ini dilisensikan di bawah lisensi [MIT](LICENSE) - bebas digunakan untuk kepentingan edukasi, pembelajaran mandiri, dan pengembangan portofolio.
