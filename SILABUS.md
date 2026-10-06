# 🗺️ Silabus Lengkap: Fullstack Data Mining (From Zero to Hero)

> **Kurikulum Berbasis Modul Mandiri (*Self-Paced Learning*)**  
> *Didesain khusus untuk pemula dan pembelajar awam yang ingin menguasai data mining mulai dari dasar konseptual, implementasi kode di Google Colab, hingga mendeploy model menjadi aplikasi web interaktif yang siap pakai.*

---

## 🧭 Peta Jalan Pembelajaran (*Learning Roadmap*)

Kurikulum ini tidak dibatasi oleh jumlah pertemuan kaku di kelas formal. Anda dapat mempelajarinya sesuai kecepatan masing-masing (*self-paced*). Setiap modul dirancang berurutan (**step-by-step**) dengan pendekatan:
1. **Analogi Dunia Nyata** (memahami intuisi tanpa pusing rumus rumit).
2. **Hands-On Google Colab** (langsung mempraktikkan kode baris demi baris).
3. **Studi Kasus Nyata** (menggunakan dataset riil industri).
4. **Fullstack Mindset** (tidak berhenti di file notebook, melainkan dikemas menjadi web app interaktif).

```
   [ LEVEL 0: FONDASI ]
   Modul 00: Mindset & Google Colab Onboarding
         │
         ▼
   Modul 01: Fondasi Python & Data Exploration (Pandas, Numpy, Viz)
         │
         ▼
   [ LEVEL 1: PREPARATION & INSIGHT ]
   Modul 02: Data Cleaning & Preprocessing (Missing Values, Outliers, Scaling)
         │
         ▼
   Modul 03: Exploratory Data Analysis (EDA) & Feature Engineering
         │
         ▼
   [ LEVEL 2: ALGORITMA CORE DATA MINING ]
   Modul 04: Supervised Learning I - Klasifikasi (KNN, Naive Bayes, Decision Tree, Random Forest)
         │
         ▼
   Modul 05: Supervised Learning II - Regresi (Linear, Polynomial, Random Forest Regressor)
         │
         ▼
   Modul 06: Unsupervised Learning I - Klasterisasi (K-Means, Hierarchical, DBSCAN, PCA)
         │
         ▼
   Modul 07: Unsupervised Learning II - Aturan Asosiasi (Apriori & FP-Growth / Market Basket)
         │
         ▼
   Modul 08: Deteksi Anomali & Dasar Text Mining (Isolation Forest & NLP Dasar)
         │
         ▼
   [ LEVEL 3: FULLSTACK HERO ]
   Modul 09: Hyperparameter Tuning, Pipeline & Serialisasi Model (Joblib/Pickle)
         │
         ▼
   Modul 10: Membangun & Mendeploy Web App Interaktif (Streamlit & Cloud Deploy)
         │
         ▼
   Modul 11: Capstone Project Akhir & Portofolio GitHub Profesional
```

---

## 📚 Rincian Modul Pembelajaran

---

### 📦 Modul 00: Mindset Data Mining & Google Colab Onboarding
*Tujuan: Memahami filosofi data mining, membedakannya dari disiplin ilmu serumpun, serta menguasai ekosistem Google Colab tanpa perlu ribet instalasi lokal.*

* **0.1 Apa Itu Data Mining Sebenarnya?**
  * Analogi "Mendulang Emas di Sungai Lumpur": Mengubah data mentah menjadi wawasan bisnis (*actionable insights*).
  * Perbedaan Data Mining vs Data Science vs Machine Learning vs Database Query (SQL).
  * Standar Siklus Kerja Industri: Metodologi **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*):
    1. *Business Understanding*
    2. *Data Understanding*
    3. *Data Preparation*
    4. *Modeling*
    5. *Evaluation*
    6. *Deployment*
* **0.2 Mengapa Menggunakan Google Colab?**
  * Keuntungan: Gratis, berbasis cloud, spesifikasi tinggi (RAM & CPU/GPU gratis), tidak membebani laptop pemula.
  * Antarmuka Colab: Memahami *Code Cell* vs *Markdown Cell*, cara menjalankan kode (`Shift + Enter`).
  * Shortcut produktivitas esensial di Colab.
* **0.3 Manajemen File & Ekosistem Colab**
  * Cara menghubungkan Colab dengan Google Drive (`drive.mount('/content/drive')`).
  * Mengunggah dataset lokal ke Colab (`files.upload()`) atau mengunduh dataset via URL / `wget`.
  * Menginstal pustaka eksternal dengan perintah bash (`!pip install <nama_pustaka>`).
* **🎯 Latihan Mandiri Modul 00:**
  * Membuat notebook Colab pertama, menuliskan deskripsi profil diri dengan format Markdown rapi, dan menjalankan perintah Python sederhana untuk menampilkan informasi sistem.

---

### 📦 Modul 01: Fondasi Python & Manipulasi Data untuk Pemula
*Tujuan: Menguasai sintaks dasar Python yang sering digunakan dalam penambangan data serta manipulasi tabel menggunakan Pandas dan visualisasi data.*

* **1.1 Python Esensial untuk Data (Bebas Teori Rumit)**
  * Tipe data: Integer, Float, String, Boolean.
  * Struktur data penting: List, Dictionary, Tuple, dan manipulasi index/slicing.
  * Logika percabangan (`if-elif-else`) dan perulangan ringkas (`for loop`, *List Comprehension*).
  * Menulis fungsi (*Functions*) dengan parameter & *return value*.
* **1.2 Bekerja dengan Tabel Menggunakan Pandas**
  * Perbedaan `Series` (1 dimensi) dan `DataFrame` (2 dimensi).
  * Membaca file data: `pd.read_csv()`, `pd.read_excel()`, `pd.read_json()`.
  * Inspeksi awal: `.head()`, `.tail()`, `.info()`, `.describe()`, `.shape`, `.dtypes`.
  * Pemilihan data: Menggunakan `.loc[]`, `.iloc[]`, dan *boolean filtering* (contoh: menyaring nasabah dengan umur > 30 tahun).
  * Transformasi data: Menambah kolom baru, menghapus kolom (`.drop()`), agregasi (`.groupby()`), dan pengurutan (`.sort_values()`).
* **1.3 Komputasi Numerik dengan NumPy**
  * Konsep NumPy Array vs List bawaan Python.
  * Operasi matematika vektor: penjumlahan, perkalian matriks, fungsi statistik (`np.mean()`, `np.std()`, `np.percentile()`).
* **1.4 Visualisasi Data Sederhana (Matplotlib & Seaborn)**
  * Membuat plot dasar: Bar Chart, Line Chart, Histogram, dan Scatter Plot.
  * Menyesuaikan judul, label sumbu, ukuran kanvas, dan palet warna.
  * Heatmap korelasi sederhana untuk melihat hubungan antar kolom numerik.
* **🎯 Studi Kasus Modul 01:**
  * Mengimpor dataset penjualan ritel (Retail Sales Data) di Colab, lalu mencari produk terlaris, bulan dengan omset tertinggi, serta memvisualisasikannya dalam diagram batang dan garis.

---

### 📦 Modul 02: Data Cleaning & Preprocessing (Jantung Data Mining)
*Tujuan: Memahami prinsip "Garbage In, Garbage Out" serta mampu membersihkan dan menyiapkan data mentah yang berantakan agar layak diproses oleh algoritma.*

* **2.1 Penanganan Nilai Hilang (*Missing Values*)**
  * Mengidentifikasi data hilang: `.isna().sum()`, visualisasi data kosong dengan `missingno`.
  * Memahami jenis missing values: MCAR (*Missing Completely at Random*), MAR, MNAR.
  * Strategi penanganan:
    * Kapan boleh menghapus baris/kolom (`.dropna()`)?
    * Imputasi statistik: Mean, Median (untuk data skew/miring), Modus (untuk data kategorikal).
    * Imputasi berbasis model: `SimpleImputer` dan `KNNImputer` dari Scikit-Learn.
* **2.2 Deteksi & Penanganan Pencilan (*Outliers*)**
  * Apa itu outlier dan dampaknya terhadap model machine learning?
  * Deteksi visual: Boxplot dan Scatter Plot.
  * Deteksi matematis: Metode **IQR** (*Interquartile Range*) dan metode **Z-Score**.
  * Teknik penanganan: Pemotongan (*Trimming*), Pembatasan nilai (*Winsorizing / Capping*).
* **2.3 Transformasi & Penskalaan Data Numerik (*Feature Scaling*)**
  * Mengapa algoritma berbasis jarak (seperti KNN, K-Means, SVM) mewajibkan penskalaan?
  * **Min-Max Normalization** (`MinMaxScaler`): Mengubah rentang nilai menjadi 0 hingga 1.
  * **Standardization** (`StandardScaler`): Mengubah data menjadi rata-rata 0 dan standar deviasi 1 (distribusi normal baku).
  * **RobustScaler**: Penskalaan yang kebal terhadap outlier ekstrem.
* **2.4 Pengkodean Data Kategorikal (*Categorical Encoding*)**
  * **Label / Ordinal Encoding**: Untuk kategori yang memiliki hierarki/peringkat (contoh: SD < SMP < SMA).
  * **One-Hot Encoding**: Untuk kategori nominal tanpa hierarki (contoh: Warna: Merah, Hijau, Biru) menggunakan `pd.get_dummies()` atau `OneHotEncoder`.
  * Menghindari perangkap jebakan multikolinearitas (*Dummy Variable Trap*).
* **🎯 Studi Kasus Modul 02:**
  * Membersihkan dataset riil pasien rumah sakit atau nasabah bank yang penuh dengan missing value, nilai salah ketik, outlier ekstrem, dan kolom teks heterogen.

---

### 📦 Modul 03: Exploratory Data Analysis (EDA) & Feature Engineering
*Tujuan: Mampu menggali cerita dan pola tersembunyi dari dataset serta merekayasa fitur baru yang meningkatkan akurasi model.*

* **3.1 Alur Kerja EDA Terstruktur**
  * Analisis Univariat: Mengetahui distribusi satu per satu variabel (Skewness, Kurtosis).
  * Analisis Bivariat: Mengetahui hubungan 2 variabel (Korelasi Pearson vs Spearman, Cross-tabulation).
  * Analisis Multivariat: Pairplot, Heatmap korelasi matriks.
* **3.2 Seni Rekayasa Fitur (*Feature Engineering*)**
  * Ekstraksi Fitur Tanggal & Waktu: Memecah `datetime` menjadi Hari, Jam, Hari Kerja vs Akhir Pekan, Kuartal.
  * Pengelompokan Nilai (*Binning / Discretization*): Mengubah umur kontinu menjadi kategori (Remaja, Dewasa, Lansia).
  * Pembuatan Fitur Rasio & Agregasi: Contoh: Rasio Utang terhadap Penghasilan (*Debt-to-Income Ratio*).
* **3.3 Seleksi Fitur (*Feature Selection*)**
  * Bahaya *Curse of Dimensionality* (terlalu banyak kolom membuat model lambat dan rentan *overfitting*).
  * Filter Methods: Analisis korelasi tinggi antar fitur independen (*Multicollinearity*).
  * Embedded Methods: Memeriksa *Feature Importance* dari model berbasis pohon.
* **🎯 Studi Kasus Modul 03:**
  * Melakukan EDA komprehensif pada dataset Titanic atau Penumpang Pesawat untuk menemukan faktor kunci yang menentukan keselamatan atau kepuasan penumpang.

---

### 📦 Modul 04: Supervised Learning I – Klasifikasi (*Classification*)
*Tujuan: Memahami intuisi, matematika dasar, implementasi kode, dan metrik evaluasi algoritma prediksi kategori/label diskrit.*

* **4.1 Konsep Dasar Klasifikasi & Partisi Data**
  * Perbedaan Data Latih (*Training Set*) dan Data Uji (*Testing Set*).
  * Pembagian data menggunakan `train_test_split` dan parameter `stratify` untuk menjaga proporsi kelas.
  * Memahami fenomena *Overfitting* (menghafal) vs *Underfitting* (kurang belajar).
* **4.2 Algoritma Klasifikasi Populer**
  * **K-Nearest Neighbors (k-NN)**:
    * Intuisi: "Karaktermu ditentukan oleh siapa tetangga terdekatmu".
    * Perhitungan jarak Euclidean dan Manhattan.
    * Memilih nilai K ganjil terbaik.
  * **Naive Bayes (Gaussian & Multinomial)**:
    * Intuisi: Teorema Bayes dan asumsi independensi bersyarat.
    * Keunggulan: Sangat cepat, efisien, handal untuk data teks/spam.
  * **Decision Tree (Pohon Keputusan)**:
    * Intuisi: Alur pengambilan keputusan bercabang (*if-then-else*).
    * Konsep Gini Impurity dan Entropy / Information Gain.
    * Visualisasi pohon keputusan dengan Scikit-Learn.
  * **Random Forest (Ensemble Learning)**:
    * Intuisi: "Musyawarah mufakat sekelompok pohon jauh lebih bijak daripada satu pohon tunggal".
    * Konsep *Bagging* (*Bootstrap Aggregating*) dan pemilihan fitur acak.
* **4.3 Evaluasi Model Klasifikasi Secara Tuntas**
  * Mengapa **Accuracy** bisa menipu pada kasus data tidak seimbang (*Imbalanced Data*)?
  * Membedah **Confusion Matrix**: True Positive (TP), False Positive (FP), True Negative (TN), False Negative (FN).
  * **Precision** vs **Recall**: Kapan memprioritaskan Precision (contoh: spam filter) dan kapan Recall (contoh: deteksi kanker/penyakit kritis)?
  * **F1-Score** dan **ROC-AUC Score**.
  * Teknik menangani kelas tidak seimbang: **SMOTE** (*Synthetic Minority Over-sampling Technique*) menggunakan pustaka `imblearn`.
* **🎯 Studi Kasus Modul 04:**
  * Membangun model prediksi resiko kredit macet (*Loan Default Prediction*) dengan membandingkan performa k-NN, Naive Bayes, Decision Tree, dan Random Forest.

---

### 📦 Modul 05: Supervised Learning II – Regresi (*Regression*)
*Tujuan: Memahami dan mengimplementasikan algoritma prediksi nilai angka kontinu (prediksi harga, penjualan, durasi).*

* **5.1 Simple & Multiple Linear Regression**
  * Intuisi garis tren terbaik: Formula $Y = \beta_0 + \beta_1 X + \epsilon$.
  * Metode *Ordinary Least Squares (OLS)*: Meminimalkan jarak selisih kuadrat residual.
  * Interpretasi Koefisien dan Intersep dalam bahasa bisnis.
* **5.2 Non-Linear & Polynomial Regression**
  * Ketika hubungan antar variabel tidak berbentuk garis lurus melainkan kurva.
  * Menambahkan fitur polinomial dengan `PolynomialFeatures`.
* **5.3 Tree-Based Regressor**
  * **Decision Tree Regressor** dan **Random Forest Regressor** untuk data non-linear berdimensi tinggi.
* **5.4 Metrik Evaluasi Regresi**
  * **MAE** (*Mean Absolute Error*): Rata-rata selisih absolut (mudah dipahami pembisnis).
  * **MSE** (*Mean Squared Error*) & **RMSE** (*Root Mean Squared Error*): Memberi penalti berat pada error besar.
  * **R-Squared ($R^2$)** & **Adjusted $R^2$**: Mengukur seberapa besar variansi target mampu dijelaskan oleh fitur.
* **🎯 Studi Kasus Modul 05:**
  * Prediksi estimasi harga mobil bekas atau harga rumah berdasarkan tahun produksi, jarak tempuh, kapasitas mesin, dan lokasi.

---

### 📦 Modul 06: Unsupervised Learning I – Klasterisasi (*Clustering*) & Reduksi Dimensi
*Tujuan: Mengelompokkan data tanpa target label untuk menemukan segmen pelanggan atau pola alami yang tersembunyi.*

* **6.1 K-Means Clustering**
  * Intuisi: Memilih $K$ titik pusat (*centroid*), mengelompokkan data ke centroid terdekat, dan memperbarui posisi centroid secara berulang.
  * Menentukan jumlah cluster optimal: **Elbow Method** (*Inertia*) dan **Silhouette Analysis**.
  * Keterbatasan K-Means: Sensitif terhadap outlier dan bentuk klaster non-lingkaran.
* **6.2 Hierarchical Clustering (Agglomerative)**
  * Intuisi pendekatan *bottom-up*: Dari setiap titik berdiri sendiri hingga bergabung menjadi satu pohon besar.
  * Membaca dan memotong **Dendrogram** untuk menentukan jumlah kelompok.
* **6.3 DBSCAN (*Density-Based Spatial Clustering of Applications with Noise*)**
  * Intuisi: Mengelompokkan berdasarkan kepadatan titik, bukan jarak pusat semata.
  * Keunggulan emas: Otomatis mendeteksi data pencilan/noise tanpa dipaksa masuk ke dalam kelompok.
  * Parameter penting: `eps` (radius) dan `min_samples`.
* **6.4 Reduksi Dimensi dengan PCA (*Principal Component Analysis*)**
  * Mengompresi puluhan kolom fitur menjadi 2 atau 3 komponen utama (*Principal Components*) tanpa kehilangan informasi penting.
  * Visualisasi klaster dalam grafik 2D dan 3D interaktif.
* **🎯 Studi Kasus Modul 06:**
  * Segmentasi Pelanggan Toko Online berdasarkan Recency, Frequency, Monetary (Analisis RFM) untuk menentukan strategi promosi yang tepat sasaran.

---

### 📦 Modul 07: Unsupervised Learning II – Aturan Asosiasi (*Association Rule Mining*)
*Tujuan: Menemukan pola keranjang belanja (*Market Basket Analysis*) untuk rekomendasi produk dan tata letak toko.*

* **7.1 Konsep Dasar Analisis Keranjang Belanja**
  * Mengapa aturan "Jika membeli produk A, maka kemungkinan besar akan membeli produk B" bernilai milyaran rupiah bagi supermarket & e-commerce.
  * Metrik Inti:
    * **Support**: Seberapa sering kombinasi item muncul dalam total transaksi.
    * **Confidence**: Seberapa sering item B dibeli saat item A dibeli.
    * **Lift Ratio**: Mengukur kekuatan aturan dibandingkan jika item dibeli secara kebetulan (Lift > 1 = asosiasi positif kuat).
* **7.2 Algoritma Apriori**
  * Prinsip Apriori: "Jika suatu itemset tidak sering muncul (*infrequent*), maka seluruh subset-nya juga tidak akan sering muncul".
  * Mengubah data transaksi kasir menjadi matriks *One-Hot Transaction* menggunakan `TransactionEncoder`.
  * Implementasi dengan pustaka `mlxtend`.
* **7.3 Algoritma FP-Growth (*Frequent Pattern Growth*)**
  * Mengapa FP-Growth jauh lebih cepat dan hemat memori daripada Apriori pada transaksi besar (*Big Data*).
* **🎯 Studi Kasus Modul 07:**
  * Menganalisis log transaksi ribuan struk belanja kasir swalayan untuk merancang paket bundling diskon dan tata letak rak barang.

---

### 📦 Modul 08: Deteksi Anomali & Dasar Text Mining
*Tujuan: Memperluas keahlian data mining ke deteksi penipuan/keanehan sistem dan pengolahan data teks bebas.*

* **8.1 Deteksi Anomali dengan Isolation Forest**
  * Intuisi: Data anomali/asing lebih sedikit dan berbeda, sehingga lebih mudah diisolasi/dipisahkan dengan sedikit pemotongan pohon keputusan.
  * Studi Kasus: Deteksi transaksi kartu kredit mencurigakan (*Fraud Detection*).
* **8.2 Pengantar Text Mining & NLP Dasar**
  * Karakteristik data teks: Tidak terstruktur (*unstructured data*).
  * Tahapan Text Preprocessing: *Case folding*, *Tokenizing*, *Stopword Removal*, dan *Stemming/Lemmatization*.
  * Representasi Teks Numerik: **Bag of Words (BoW)** dan **TF-IDF** (*Term Frequency - Inverse Document Frequency*).
  * Klasifikasi Teks Sederhana: Analisis sentimen ulasan produk (Positif vs Negatif) menggunakan Naive Bayes.
* **🎯 Studi Kasus Modul 08:**
  * Menganalisis ribuan ulasan aplikasi di Google Play Store atau toko online untuk mendeteksi sentimen kepuasan pengguna.

---

### 📦 Modul 09: Hyperparameter Tuning, Pipeline & Serialisasi Model
*Tujuan: Mengoptimalkan model ke performa puncak dan mengemas alur kerja data mining menjadi artefak yang dapat diintegrasikan dengan aplikasi lain.*

* **9.1 Validasi Silang (*K-Fold Cross-Validation*)**
  * Menghindari bias pemilihan data uji acak dengan membagi data menjadi $K$ lipatan bergilir.
* **9.2 Penyetelan Hyperparameter (*Hyperparameter Tuning*)**
  * **GridSearchCV**: Mencoba seluruh kombinasi parameter secara sistematis.
  * **RandomizedSearchCV**: Mencari kombinasi parameter terbaik secara acak (jauh lebih cepat untuk ruang parameter besar).
* **9.3 Scikit-Learn Pipeline**
  * Mengapa pipeline krusial? Mencegah kebocoran data (*Data Leakage*) saat preprocessing.
  * Menggabungkan Imputer, Scaler, Encoder, dan Model Klasifikasi menjadi satu objek `Pipeline` yang elegan.
* **9.4 Serialisasi Model: Menyimpan & Memuat Kembali Model**
  * Menyimpan pipeline model terlatih ke disk menggunakan pustaka `joblib` atau `pickle` (`model.pkl`).
  * Menguji memuat ulang model di skrip terpisah untuk memprediksi data masukan baru (*Inference*).
* **🎯 Latihan Modul 09:**
  * Membuat pipeline utuh dari data mentah hingga penyimpanan file model `best_model.joblib`.

---

### 🚀 Modul 10: The Fullstack Milestone – Membangun & Mendeploy Web App Interaktif
*Tujuan: Mengubah file notebook menjadi aplikasi web interaktif yang hidup, fungsional, dan dapat diakses siapa saja melalui internet.*

* **10.1 Mengapa Model Data Mining Harus Dibuatkan Web App?**
  * Klien, manajer, atau rekan kerja non-teknis tidak bisa membaca file notebook `.ipynb`. Mereka membutuhkan antarmuka visual interaktif yang ramah pengguna.
* **10.2 Mengenal Streamlit (Python Web Framework untuk Praktisi Data)**
  * Keunggulan Streamlit: Murni kode Python, tanpa perlu HTML/CSS/JavaScript rumit, reaktif secara otomatis.
  * Elemen Input Streamlit: `st.title()`, `st.slider()`, `st.selectbox()`, `st.number_input()`, `st.file_uploader()`.
  * Visualisasi Interaktif: Menampilkan grafik Plotly, diagram Matplotlib, dan tabel DataFrame interaktif.
* **10.3 Arsitektur Web App Data Mining**
  * Membaca file model `model.joblib` yang telah disimpan dari Colab.
  * Menerima input dari pengguna melalui formulir web.
  * Melakukan prediksi secara real-time dan menampilkan hasil diagnosis/rekomendasi beserta probabilitasnya.
  * Fitur Batch Prediction: Pengguna dapat mengunggah file CSV data baru, lalu aplikasi otomatis memproses dan menyediakan tombol unduh hasil prediksi.
* **10.4 Menguji Streamlit Langsung dari Google Colab**
  * Menjalankan server Streamlit di Colab menggunakan terowongan `localtunnel` atau `ngrok` untuk pratinjau cepat tanpa instalasi lokal.
* **10.5 Deployment Gratis ke Streamlit Community Cloud**
  * Menghubungkan repositori GitHub dengan Streamlit Cloud.
  * Menyusun file `requirements.txt` yang tepat agar aplikasi berjalan mulus di server cloud.
  * Mendapatkan URL publik gratis (contoh: `https://nama-aplikasi.streamlit.app`) untuk dicantumkan di CV & LinkedIn!
* **🎯 Proyek Modul 10:**
  * Membangun aplikasi web kalkulator prediksi resiko penyakit jantung atau prediksi kelayakan kredit nasabah yang online dan responsif.

---

### 🏆 Modul 11: Capstone Project Akhir & Portofolio Ready
*Tujuan: Mengerjakan proyek data mining end-to-end secara mandiri dari nol hingga tayang, serta mendokumentasikannya secara profesional di GitHub.*

* **11.1 Memilih Masalah & Dataset Nyata**
  * Sumber dataset berkualitas: Kaggle, UCI Machine Learning Repository, Satu Data Indonesia, Google Dataset Search.
  * Memilih 1 domain masalah: Finansial, Layanan Kesehatan, Ritel/E-commerce, atau Pendidikan.
* **11.2 Eksekusi Alur CRISP-DM Lengkap**
  1. Identifikasi masalah dan rumusan pertanyaan bisnis.
  2. Exploratory Data Analysis & visualisasi insight.
  3. Preprocessing, penanganan missing value, dan rekayasa fitur.
  4. Eksperimen perbandingan minimal 3 algoritma data mining.
  5. Evaluasi performa mendalam dan analisis matriks kebingungan (*confusion matrix*).
  6. Penyimpanan model pipeline terbaik.
  7. Pembuatan antarmuka web interaktif dengan Streamlit.
  8. Deployment live ke cloud publik.
* **11.3 Panduan Showcase Portofolio di GitHub**
  * Menulis file `README.md` repositori proyek yang memukau: Deskripsi masalah, demo GIF/video aplikasi, arsitektur data, petunjuk instalasi, dan tautan live app.
  * Tips memasukkan proyek ke resume/CV dan LinkedIn untuk menarik minat perekrut (*recruiter*).

---

## 🛠️ Ringkasan Alat & Pustaka (*Tech Stack*)

| Kategori | Alat / Pustaka | Fungsi Utama |
| :--- | :--- | :--- |
| **Platform Eksekusi** | Google Colab | Lingkungan komputasi berbasis cloud gratis dengan akses CPU/GPU. |
| **Manipulasi & Perhitungan** | Pandas, NumPy | Membaca tabel, membersihkan kolom, dan kalkulasi array numerik. |
| **Visualisasi Data** | Matplotlib, Seaborn, Plotly | Membuat grafik statis dan diagram interaktif. |
| **Core Data Mining & ML** | Scikit-Learn | Klasifikasi, regresi, klasterisasi, preprocessing, dan pipeline. |
| **Aturan Asosiasi** | MLxtend | Algoritma Apriori & FP-Growth untuk *market basket analysis*. |
| **Pembersihan Missing Data** | Missingno | Visualisasi pola data hilang pada dataset. |
| **Imbalanced Data** | Imbalanced-learn (SMOTE) | Menangani ketidakseimbangan kelas data. |
| **Penyimpanan Model** | Joblib | Menyimpan dan memuat objek model machine learning. |
| **Antarmuka Web App** | Streamlit | Membangun dashboard dan web aplikasi interaktif dengan Python murni. |
| **Deployment Cloud** | Streamlit Community Cloud | Mempublikasikan aplikasi web ke internet secara gratis. |
| **Version Control & Sharing**| Git & GitHub | Mengelola kode sumber, melacak revisi, dan portofolio publik. |

---

## 💡 Tips Belajar untuk Pemula Awam

1. **Jangan Hafalkan Rumus Matematis**: Fokus pada **intuisi** ("mengapa algoritma ini memilih memotong cabang pohon ini?", "mengapa jarak euclidean sensitif terhadap perbedaan skala harga vs umur?").
2. **Ketik Ulang Kode, Jangan Sekadar Copy-Paste**: Mengetik ulang baris kode melatih memori otot jari dan kepekaan terhadap kesalahan ketik (*syntax error*).
3. **Bersahabatlah dengan Error**: Ketika muncul teks merah di Colab, jangan panik! Gulir ke baris paling bawah, baca nama error-nya (misal: `KeyError`, `ValueError`, `IndexError`), dan cari tahu penyebabnya.
4. **Learn in Public**: Setiap kali menyelesaikan satu modul, buat postingan rangkuman di LinkedIn atau bagikan cuplikan notebook di GitHub. Konsistensi kecil yang dilakukan terus-menerus akan membawa Anda dari **Zero** menjadi **Hero**!
