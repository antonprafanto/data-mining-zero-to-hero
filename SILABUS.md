# 🗺️ Silabus Lengkap: Fullstack Data Mining (From Zero to Hero)

> **Kurikulum Berbasis Modul Mandiri (*Self-Paced Learning*)**  
> *Didesain khusus untuk pemula dan pembelajar awam yang ingin menguasai data mining mulai dari dasar konseptual, implementasi kode di Google Colab, hingga mendeploy model menjadi aplikasi web interaktif yang siap pakai.*

---

## 📖 Kamus Istilah Awam (*Jargon Buster*)

Bagi Anda yang baru pertama kali terjun ke dunia data, jangan biarkan istilah teknis bahasa Inggris membuat Anda takut. Gunakan kamus analogi ini sebagai pegangan:

| Istilah Teknis | Bahasa Sederhana | Analogi Dunia Nyata |
| :--- | :--- | :--- |
| **Dataset** | Tabel Kumpulan Data | Buku catatan besar atau lembar Excel berisi baris dan kolom. |
| **Feature (Fitur / Atribut)** | Ciri-ciri / Variabel Input | Karakteristik fisik seseorang (tinggi badan, warna rambut, usia). |
| **Target / Label** | Kunci Jawaban / Hasil Tebakan | Hasil diagnosis dokter (Positif Sakit / Sehat). |
| **Supervised Learning** | Belajar dengan Guru | Belajar mengerjakan soal ujian yang di bagian belakang bukunya sudah ada kunci jawabannya. |
| **Unsupervised Learning** | Belajar Tanpa Guru | Diberi sekotak kancing acak lalu diminta mengelompokkan sendiri berdasarkan kesamaan warna/bentuk tanpa diberi tahu nama kancingnya. |
| **Training Data (Data Latih)** | Bahan Latihan Belajar | Kumpulan soal latihan yang dikerjakan siswa sebelum hari ujian. |
| **Testing Data (Data Uji)** | Lembar Ujian Asli | Soal ujian akhir semester yang belum pernah dilihat siswa untuk menguji kepintarannya. |
| **Overfitting** | Menghafal Mati (Terlalu Kaku) | Siswa yang menghafal persis angka soal latihan. Saat angka diganti sedikit di hari ujian, ia langsung panik dan gagal. |
| **Underfitting** | Kurang Belajar (Terlalu Malas) | Siswa yang malas membaca buku, sehingga polanya saja tidak tahu. |
| **Data Leakage** | Mencontek Bocoran Soal | Tanpa sengaja melihat kunci jawaban ujian saat masih sesi latihan, sehingga terkesan pintar padahal mencontek. |
| **Hyperparameter** | Tombol Setelan / Kenop Mesin | Tombol pengatur suhu pada oven kue atau kenop frekuensi radio untuk mencari sinyal paling jernih. |
| **Inference / Deployment** | Terjun ke Lapangan Nyata | Membawa mesin/model yang sudah pintar keluar dari lab untuk melayani pengguna asli di web. |

---

## 🧭 Peta Jalan Pembelajaran (*Learning Roadmap*)

Kurikulum ini tidak dibatasi oleh jumlah pertemuan kaku di kelas formal. Anda dapat mempelajarinya sesuai kecepatan masing-masing (*self-paced*).

```
   [ LEVEL 0: FONDASI ]
   Modul 00: Mindset Data Mining, KDD, CRISP-DM & Google Colab Lifehacks
         │
         ▼
   Modul 01: Fondasi Python & Data Exploration (Pandas, Numpy, Seaborn)
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
   Modul 11: Capstone Project Akhir, Etika Data & Portofolio GitHub Profesional
```

---

## 📚 Rincian Modul Pembelajaran

---

### 📦 Modul 00: Mindset Data Mining & Google Colab Onboarding
*Tujuan: Memahami filosofi data mining, membedakannya dari disiplin ilmu serumpun, menguasai 2 tugas pokok (Prediktif vs Deskriptif), 4 tipe data dunia nyata, serta menguasai ekosistem Google Colab tanpa perlu ribet instalasi lokal.*

* **0.1 Apa Itu Data Mining Sebenarnya?**
  * Analogi "Mendulang Emas di Sungai Keruh": Mengubah tumpukan data mentah (*raw data*) menjadi wawasan bisnis (*actionable insights*).
  * Fenomena *"Data rich, but information poor"* di era modern.
  * Perbedaan Data Mining vs Machine Learning vs Artificial Intelligence vs Data Science.
* **0.2 Dua Tugas Pokok Data Mining: Prediktif vs Deskriptif**
  * **Tugas Prediktif**: Memiliki target (*supervised*) untuk menebak masa depan.
    * Klasifikasi (memprediksi label kategori, e.g., Spam vs Bukan Spam).
    * Regresi (memprediksi angka kontinu, e.g., estimasi harga rumah).
  * **Tugas Deskriptif**: Menemukan pola alami tersembunyi tanpa target (*unsupervised*).
    * Klasterisasi (pengelompokan segmen data mirip).
    * Aturan Asosiasi (*Market Basket Analysis* / barang yang dibeli bersamaan).
    * Deteksi Anomali (menemukan kejanggalan/fraud).
* **0.3 Kapan Butuh Data Mining & Kapan Cukup Rumus/SQL Biasa?**
  * Kapan **tidak perlu** data mining: masalah berpola pasti yang bisa dihitung dengan rumus matematika pasti atau query SQL biasa.
  * Kapan **wajib** data mining: data besar, polanya tersembunyi (*unknown pattern*), dan relasi antar variabel terlalu kompleks bagi logika manusia biasa.
* **0.4 Dua Metodologi Standar: KDD vs CRISP-DM**
  * Metodologi Akademik: **KDD** (*Knowledge Discovery in Databases*): Selection, Cleaning, Transformation, Data Mining, Pattern Evaluation.
  * Metodologi Industri: **CRISP-DM** (Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment).
* **0.5 Fondasi Mutlak: 4 Tipe Data Dunia Nyata**
  * Numerik Kontinu (pecahan/desimal) vs Numerik Diskrit (angka bulat hasil hitungan).
  * Kategorikal Nominal (tanpa tingkatan) vs Kategorikal Ordinal (memiliki hierarki peringkat).
* **0.6 Mengapa Menggunakan Google Colab & Anatomi Antarmuka**
  * Keuntungan komputasi awan gratis, RAM & CPU/GPU gratis, tidak membebani laptop pemula.
  * Antarmuka Colab: Bilah sisi 📁 (*Files Explorer*), status RAM & Disk, CPU vs GPU gratis.
  * Sel Teks (*Markdown*) vs Sel Kode (*Python*), shortcut produktivitas esensial (`Shift + Enter`, `Esc B`, `Esc DD`).
  * Aturan Emas Spasi Python (*Indentation*): Menghindari `IndentationError` bagi pemula.
* **0.7 Manajemen File & Lifehacks Colab untuk Pemula**
  * Memahami sifat sesi sementara (*ephemeral*) dan cara menghubungkan Google Drive (`drive.mount`).
  * Batasan kuota Colab gratis: batas durasi 12 jam, *idle timeout* 90 menit.
  * Membaca dataset daring langsung via URL tanpa ketergantungan OS.
  * Cara mengunduh file notebook ke harddisk komputer (`.ipynb` / `.py`).
* **🎯 Checklist Pemahaman Diri Modul 00:**
  - [ ] Saya paham analogi data mining mendulang emas dari pasir sungai keruh.
  - [ ] Saya bisa membedakan 2 tugas pokok: Prediktif (ada target) vs Deskriptif (tanpa target).
  - [ ] Saya tahu kapan masalah butuh data mining dan kapan cukup rumus kalkulasi biasa.
  - [ ] Saya paham 4 tipe data: Kontinu, Diskrit, Nominal, dan Ordinal.
  - [ ] Saya hafal alur KDD (5 tahap) dan CRISP-DM (6 tahap).
  - [ ] Saya bisa membuka Google Colab, menjalankan kode, dan tahu cara mengunduh notebook.

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
* **🎯 Checklist Pemahaman Diri Modul 01:**
  - [ ] Saya bisa memuat file CSV ke DataFrame Pandas.
  - [ ] Saya bisa memfilter baris tertentu dan mengelompokkan data dengan `.groupby()`.
  - [ ] Saya bisa membuat grafik diagram batang dan histogram sebaran data dengan Seaborn.

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
* **🎯 Checklist Pemahaman Diri Modul 02:**
  - [ ] Saya tahu kapan harus mengisi missing value dengan median daripada mean.
  - [ ] Saya bisa mendeteksi batas outlier menggunakan rumus IQR ($Q1 - 1.5 \times IQR$ dan $Q3 + 1.5 \times IQR$).
  - [ ] Saya paham mengapa kita perlu menstandarkan skala umur (puluhan) dan gaji (jutaan) sebelum melatih model.

---

### 📦 Modul 03: Exploratory Data Analysis (EDA) & Feature Engineering
*Tujuan: Mampu menggali cerita dan pola tersembunyi dari dataset serta merekayasa fitur baru yang meningkatkan performa model.*

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
* **🎯 Checklist Pemahaman Diri Modul 03:**
  - [ ] Saya bisa membaca heatmap korelasi dan mengidentifikasi fitur yang paling berpengaruh terhadap target.
  - [ ] Saya mampu membuat fitur turunan baru yang bermakna dari data tanggal dan teks.
  - [ ] Saya tahu fitur mana yang harus dibuang karena redundan.

---

### 📦 Modul 04: Supervised Learning I – Klasifikasi (*Classification*)
*Tujuan: Memahami intuisi, implementasi kode, dan metrik evaluasi algoritma prediksi kategori/label diskrit.*

* **4.1 Konsep Dasar Klasifikasi & Partisi Data**
  * Perbedaan Data Latih (*Training Set*) dan Data Uji (*Testing Set*).
  * Pembagian data menggunakan `train_test_split` dan parameter `stratify` untuk menjaga proporsi kelas.
  * Memahami fenomena *Overfitting* (menghafal) vs *Underfitting* (kurang belajar).
* **4.2 Algoritma Klasifikasi Populer**
  * **K-Nearest Neighbors (k-NN)**:
    * *Analogi*: "Tebak selera musik seseorang berdasarkan selera musik 3 teman terdekatnya".
    * Perhitungan jarak Euclidean dan Manhattan.
    * Memilih nilai K ganjil terbaik.
  * **Naive Bayes (Gaussian & Multinomial)**:
    * *Analogi*: Dokter yang menghitung probabilitas pasien terkena flu berdasarkan gejala demam dan batuk secara independen.
    * Keunggulan: Sangat cepat, efisien, handal untuk data teks/spam.
  * **Decision Tree (Pohon Keputusan)**:
    * *Analogi*: Bagan alur "Buku Panduan Diagnosa" (Jika batuk > ya -> cek suhu > 38°C -> demam tinggi).
    * Konsep Gini Impurity dan Entropy / Information Gain.
  * **Random Forest (Ensemble Learning)**:
    * *Analogi*: Mengumpulkan pendapat 100 dokter spesialis lalu mengambil voting terbanyak (*majority voting*).
* **4.3 Evaluasi Model Klasifikasi Secara Tuntas**
  * Mengapa **Accuracy** bisa menipu pada kasus data tidak seimbang (*Imbalanced Data*)?
  * Membedah **Confusion Matrix**: True Positive (TP), False Positive (FP), True Negative (TN), False Negative (FN).
  * **Precision** vs **Recall**: Kapan memprioritaskan Precision (contoh: spam filter) dan kapan Recall (contoh: deteksi kanker/penyakit kritis)?
  * **F1-Score** dan **ROC-AUC Score**.
  * Teknik menangani kelas tidak seimbang: **SMOTE** (*Synthetic Minority Over-sampling Technique*).
* **🎯 Checklist Pemahaman Diri Modul 04:**
  - [ ] Saya bisa membedakan kapan harus menggunakan k-NN, Naive Bayes, Decision Tree, atau Random Forest.
  - [ ] Saya paham mengapa akurasi 99% bisa berbahaya jika data positif kanker hanya 1% dan model memprediksi semua negatif.
  - [ ] Saya bisa membaca diagram Confusion Matrix dan menghitung Precision serta Recall.

---

### 📦 Modul 05: Supervised Learning II – Regresi (*Regression*)
*Tujuan: Memahami dan mengimplementasikan algoritma prediksi nilai angka kontinu (prediksi harga, penjualan, durasi).*

* **5.1 Simple & Multiple Linear Regression**
  * *Analogi*: Makelar properti yang menaksir harga rumah: "Setiap tambah 1 meter persegi, harga naik 5 juta".
  * Formula $Y = \beta_0 + \beta_1 X + \epsilon$.
  * Metode *Ordinary Least Squares (OLS)*.
* **5.2 Non-Linear & Polynomial Regression**
  * Ketika hubungan data membentuk lengkungan/kurva, bukan garis lurus.
* **5.3 Tree-Based Regressor**
  * Menggunakan Decision Tree dan Random Forest untuk memprediksi angka kontinu.
* **5.4 Metrik Evaluasi Regresi**
  * **MAE** (*Mean Absolute Error*): Selisih rupiah/angka rata-rata yang mudah dipahami bos/manajemen.
  * **RMSE** (*Root Mean Squared Error*): Menghukum error besar dengan kuadrat.
  * **R-Squared ($R^2$)**: Menjelaskan seberapa persen variasi harga yang berhasil dijelaskan oleh model kita.
* **🎯 Checklist Pemahaman Diri Modul 05:**
  - [ ] Saya paham perbedaan mendasar Klasifikasi (kategori) dan Regresi (angka kontinu).
  - [ ] Saya bisa menginterpretasikan nilai koefisien regresi.
  - [ ] Saya bisa membedakan arti metrik MAE, RMSE, dan nilai $R^2$.

---

### 📦 Modul 06: Unsupervised Learning I – Klasterisasi (*Clustering*) & Reduksi Dimensi
*Tujuan: Mengelompokkan data tanpa target label untuk menemukan segmen pelanggan atau pola alami yang tersembunyi.*

* **6.1 K-Means Clustering**
  * *Analogi*: Membuka 3 cabang gudang logistik baru (titik pusat/centroid) agar berada paling dekat dengan rumah-rumah pelanggan di sekitarnya.
  * Menentukan jumlah cluster optimal: **Elbow Method** dan **Silhouette Score**.
* **6.2 Hierarchical Clustering (Dendrogram)**
  * *Analogi*: Pohon silsilah keluarga, dari individu hingga bertemu pada leluhur yang sama.
* **6.3 DBSCAN (*Density-Based*)**
  * *Analogi*: Menemukan kerumunan orang di stadion; orang yang menyendiri jauh di sudut tribun otomatis dianggap outlier/noise.
* **6.4 Reduksi Dimensi dengan PCA (*Principal Component Analysis*)**
  * *Analogi*: Memotret patung 3 dimensi dari sudut pandang terbaik agar bayangannya di dinding 2D tetap menampilkan bentuk patung sejelas mungkin.
* **🎯 Checklist Pemahaman Diri Modul 06:**
  - [ ] Saya paham bahwa dalam Unsupervised Learning tidak ada kolom target/label.
  - [ ] Saya bisa menentukan jumlah K optimal pada K-Means menggunakan grafik Elbow Method.
  - [ ] Saya bisa memproyeksikan data berdimensi banyak menjadi plot 2D menggunakan PCA.

---

### 📦 Modul 07: Unsupervised Learning II – Aturan Asosiasi (*Association Rule Mining*)
*Tujuan: Menemukan pola keranjang belanja (*Market Basket Analysis*) untuk strategi penataan produk dan diskon bundling.*

* **7.1 Konsep Dasar Analisis Keranjang Belanja**
  * *Analogi*: Kisah klasik supermarket: Pembeli popok bayi di hari Jumat sore sering kali membeli minuman kaleng sekaligus.
  * Metrik Inti:
    * **Support**: Seberapa populer kombinasi barang tersebut di seluruh struk kasir.
    * **Confidence**: Seberapa pasti pembeli barang A akan ikut mengambil barang B.
    * **Lift Ratio**: Ukuran kekuatan asosiasi (Lift > 1 = korelasi positif nyata, bukan kebetulan).
* **7.2 Algoritma Apriori & FP-Growth**
  * Prinsip eliminasi Apriori dan efisiensi pohon FP-Growth.
  * Menggunakan pustaka `mlxtend` pada data transaksi ritel.
* **🎯 Checklist Pemahaman Diri Modul 07:**
  - [ ] Saya bisa mengubah log transaksi belanja menjadi tabel matriks biner One-Hot.
  - [ ] Saya bisa membaca dan menafsirkan arti nilai Support, Confidence, dan Lift Ratio.

---

### 📦 Modul 08: Deteksi Anomali & Dasar Text Mining
*Tujuan: Memperluas keahlian data mining ke deteksi kecurangan sistem dan pengolahan data teks bebas.*

* **8.1 Deteksi Anomali dengan Isolation Forest**
  * *Analogi*: Satpam bank yang memeriksa ribuan slip setoran; transaksi mencurigakan (anomali) biasanya nilainya ganjil atau di jam yang tidak lazim sehingga sangat mudah dipisahkan.
* **8.2 Pengantar Text Mining & Analisis Sentimen**
  * *Analogi*: Mengubah surat ulasan pelanggan menjadi frekuensi kata numerik.
  * Text Preprocessing: *Lowercasing*, *Tokenizing*, *Stopword Removal*, *Stemming*.
  * Pembobotan **TF-IDF** (*Term Frequency - Inverse Document Frequency*).
  * Klasifikasi sentimen ulasan (Positif / Negatif) dengan Naive Bayes.
* **🎯 Checklist Pemahaman Diri Modul 08:**
  - [ ] Saya bisa menerapkan Isolation Forest untuk menandai data anomali.
  - [ ] Saya bisa membersihkan data teks dari tanda baca dan kata sambung umum (*stopwords*).
  - [ ] Saya bisa mengubah kumpulan kalimat teks menjadi matriks angka menggunakan TF-IDF.

---

### 📦 Modul 09: Hyperparameter Tuning, Pipeline & Serialisasi Model
*Tujuan: Mengoptimalkan model ke performa puncak dan mengemas alur kerja data mining menjadi artefak yang dapat diintegrasikan dengan aplikasi lain.*

* **9.1 Validasi Silang (*K-Fold Cross-Validation*)**
  * Menghindari bias pemilihan data uji acak dengan membagi data menjadi $K$ lipatan bergilir.
* **9.2 Penyetelan Hyperparameter (*Hyperparameter Tuning*)**
  * **GridSearchCV**: Mencoba seluruh kombinasi parameter secara sistematis.
  * **RandomizedSearchCV**: Mencari kombinasi terbaik secara acak (cepat dan efisien).
* **9.3 Scikit-Learn Pipeline**
  * Mengapa pipeline krusial? Menghindari *Data Leakage* dengan merangkai Imputer -> Scaler -> Model menjadi satu kesatuan rapi.
* **9.4 Serialisasi Model: Menyimpan & Memuat Model**
  * Menyimpan pipeline ke file biner (`.joblib` atau `.pkl`).
  * Menguji fungsi `joblib.load()` untuk melakukan prediksi pada data masukan baru.
* **🎯 Checklist Pemahaman Diri Modul 09:**
  - [ ] Saya bisa menyusun objek `Pipeline` Scikit-Learn dari preprocessing hingga estimator.
  - [ ] Saya bisa menggunakan GridSearchCV untuk mencari nilai parameter terbaik.
  - [ ] Saya berhasil mengekspor model menjadi file `model.joblib`.

---

### 🚀 Modul 10: The Fullstack Milestone – Web App Interaktif (Streamlit)
*Tujuan: Mengubah file notebook menjadi aplikasi web interaktif yang hidup, fungsional, dan dapat diakses siapa saja melalui internet.*

* **10.1 Mengapa Praktisi Data Mining Harus Paham Web App?**
  * Rekan kerja non-teknis dan pimpinan tidak membaca kode notebook; mereka butuh tombol, slider, dan visualisasi yang mudah dimengerti.
* **10.2 Mengenal Streamlit (Python Web Framework)**
  * Input widgets: `st.slider()`, `st.selectbox()`, `st.number_input()`, `st.file_uploader()`.
  * Menampilkan grafik interaktif Plotly dan tabel interaktif Pandas.
* **10.3 Integrasi Model Data Mining ke Web App**
  * Membaca file `model.joblib` di Streamlit.
  * Menerima input data pengguna, memproses ke pipeline, dan menampilkan hasil prediksi serta probabilitasnya.
  * Fitur unggah file CSV untuk prediksi massal (*Batch Prediction*).
* **10.4 Menjalankan Streamlit dari Google Colab**
  * Menggunakan terowongan tunnel `localtunnel` atau `ngrok` untuk melihat pratinjau web app langsung dari Colab.
* **10.5 Deployment Gratis ke Streamlit Community Cloud**
  * Menghubungkan repo GitHub ke Streamlit Cloud dan mendapatkan tautan publik gratis yang aktif 24/7.
* **🎯 Checklist Pemahaman Diri Modul 10:**
  - [ ] Saya bisa membuat skrip antarmuka Streamlit sederhana di Python.
  - [ ] Saya bisa memuat model machine learning di Streamlit dan menampilkan hasil prediksi berdasarkan input user.
  - [ ] Web app saya berhasil online dan bisa dibuka dari smartphone teman melalui link publik.

---

### 🏆 Modul 11: Capstone Project Akhir, Etika Data & Portofolio Ready
*Tujuan: Mengerjakan proyek data mining end-to-end secara mandiri dari nol hingga tayang, menerapkan etika data, serta mendokumentasikannya secara profesional di GitHub.*

* **11.1 Etika & Legalitas Penambangan Data (Data Ethics)**
  * **Prinsip Anonimitas & Privasi**: Kepatuhan terhadap UU Perlindungan Data Pribadi (UU PDP) / GDPR. Jangan menyertakan NIK, nomor telepon, alamat asli, atau data medis tanpa persetujuan (*consent*).
  * **Bias & Keadilan Algoritma (*Fairness*)**: Memastikan model tidak mendiskriminasi ras, gender, atau agama.
  * **Etika Web Scraping**: Memeriksa file `robots.txt` situs target dan tidak membebani server target secara brutal.
* **11.2 Eksekusi Alur CRISP-DM Lengkap (Capstone Project)**
  1. Identifikasi masalah dan rumusan pertanyaan bisnis.
  2. Exploratory Data Analysis & visualisasi insight.
  3. Preprocessing, penanganan missing value, dan rekayasa fitur.
  4. Eksperimen perbandingan minimal 3 algoritma data mining.
  5. Evaluasi performa mendalam dan analisis matriks kebingungan (*confusion matrix*).
  6. Penyimpanan model pipeline terbaik.
  7. Pembuatan antarmuka web interaktif dengan Streamlit.
  8. Deployment live ke cloud publik.
* **11.3 Panduan Showcase Portofolio di GitHub**
  * Menulis file `README.md` portofolio yang memikat: Judul catchy, demo GIF/video aplikasi, arsitektur data, petunjuk instalasi, dan tautan live app.
  * Cara menceritakan proyek ini saat sesi wawancara kerja (*interview technique*).
* **🎯 Checklist Akhir Kelulusan Hero:**
  - [ ] Capstone project selesai menerapkan siklus CRISP-DM lengkap dari awal hingga akhir.
  - [ ] Aplikasi web Streamlit aktif di internet dan dapat diakses publik.
  - [ ] Repositori GitHub memiliki README bintang lima dengan demonstrasi visual yang rapi.

---

## 💡 5 Aturan Emas untuk Pembelajar Awam

1. **Intuisi Lebih Penting daripada Rumus**: Jangan takut jika Anda bukan lulusan matematika. Yang terpenting adalah mengerti *mengapa* sebuah algoritma mengambil keputusan tersebut.
2. **Ketik Ulang Kodenya**: Jangan sekadar membaca atau salin-tempel. Mengetik kode membangun kebiasaan memori otot dan kepekaan terhadap typo.
3. **Pesan Error Adalah Guru Terbaik**: Ketika muncul teks merah di Colab, jangan panik! Gulir ke baris paling bawah, baca jenis error-nya, dan cari tahu penyebabnya.
4. **Jaga Konsistensi**: Luangkan 30-60 menit setiap hari daripada belajar 7 jam sekaligus seminggu sekali lalu berhenti.
5. **Learn in Public**: Bagikan kemajuan belajar Anda di LinkedIn atau GitHub. Mendokumentasikan perjalanan belajar adalah cara terbaik untuk memperkuat pemahaman sekaligus membangun personal branding!
