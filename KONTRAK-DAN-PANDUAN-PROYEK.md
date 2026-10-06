# 📜 Kontrak Belajar & Panduan Proyek: Fullstack Data Mining

Selamat datang di repositori pembelajaran **Fullstack Data Mining: From Zero to Hero**. Dokumen ini berfungsi sebagai peta komitmen dan panduan pengerjaan proyek bagi siapa saja yang ingin menguasai data mining mulai dari titik nol hingga mampu mendeploy model interaktif ke web app.

---

## 🎯 1. Filosofi & Mindset Pembelajaran

> *"Data hanyalah angka dan teks mati, hingga Anda mengekstrak cerita, pola, dan nilai yang bisa membantu manusia mengambil keputusan terbaik."*

Bagi pembelajar awam, sering muncul ketakutan terhadap matematika, statistik, atau baris kode rumit. Di kurikulum ini, kita menerapkan metode:
1. **Intuisi Dahulu, Rumus Menyusul**: Pahami *mengapa* sebuah algoritma bekerja menggunakan analogi dunia nyata sebelum membedah formula matematisnya.
2. **Hands-On Sejak Hari Pertama**: Jangan hanya membaca materi; jalankan baris kode, modifikasi parameter, dan amati langsung perubahannya.
3. **Fullstack Mindset**: Seorang penambang data modern tidak hanya berhenti di file `.ipynb` (Jupyter Notebook), melainkan mampu mengemas karyanya menjadi dashboard/aplikasi web interaktif (Streamlit) yang dapat digunakan oleh rekan kerja atau publik.
4. **Learn in Public & Version Control**: Dokumentasikan proses belajar Anda di GitHub secara bertahap dan rapi.

---

## 🤝 2. Kontrak Belajar Mandiri (*Self-Learning Agreement*)

Untuk mencapai level **Hero**, komitmen konsistensi adalah kunci utama:
- **Alokasi Waktu**: Minimal 3–5 jam per minggu untuk membaca materi, membedah dataset, dan mengerjakan latihan.
- **Kebiasaan Eksperimen**: Tidak takut melihat pesan error; jadikan pesan error (*traceback*) sebagai petunjuk terbaik untuk belajar memahami alur eksekusi program.
- **Prinsip Kejujuran Data**: Tidak memanipulasi data sembarangan hanya demi mendapatkan akurasi 99% semu (*overfitting / data leakage*).

---

## 🛠️ 3. Pedoman Penggunaan Google Colab

Seluruh materi praktik dirancang untuk dieksekusi di **Google Colab**:
1. **Tidak Memerlukan Laptop Spek Dewa**: Google Colab berjalan di cloud server Google dengan spesifikasi RAM tinggi dan akses GPU gratis.
2. **Penyimpanan Kode**: Pastikan selalu menyimpan salinan notebook ke Google Drive pribadi Anda (`File -> Save a copy in Drive`) atau simpan langsung ke GitHub (`File -> Save a copy in GitHub`).
3. **Penyimpanan Model**: File model yang telah dilatih (`.joblib` / `.pkl`) dapat diunduh langsung dari panel file Colab ke komputer lokal atau disimpan di Google Drive.

---

## 📋 4. Panduan Pengerjaan Capstone Project

Capstone Project adalah bukti nyata kemampuan Anda sebagai praktisi Fullstack Data Mining. Proyek ini harus mencakup seluruh tahapan CRISP-DM:

```
[1. Problem & Business Goal] 
             ⬇
[2. Data Collection & EDA]
             ⬇
[3. Data Preprocessing & Cleaning]
             ⬇
[4. Model Training & Comparison]
             ⬇
[5. Evaluation & Error Analysis]
             ⬇
[6. Model Export (.joblib)]
             ⬇
[7. Web App (Streamlit) & Cloud Deployment]
```

### Rubrik Penilaian Mandiri Proyek
| Kriteria | Bobot | Deskripsi |
| :--- | :---: | :--- |
| **Kejelasan Masalah & EDA** | 20% | Latar belakang masalah jelas, dataset relevan, visualisasi EDA memberikan wawasan bisnis yang tajam. |
| **Kualitas Preprocessing** | 25% | Penanganan missing values tepat, scaling sesuai jenis algoritma, categorical encoding rapi tanpa data leakage. |
| **Eksperimen & Evaluasi Model** | 25% | Membandingkan minimal 2-3 algoritma, tuning parameter, dan memilih metrik evaluasi yang tepat (bukan hanya akurasi). |
| **Aplikasi Web Interaktif (Streamlit)** | 20% | Antarmuka web ramah pengguna, menerima input data baru, dan menampilkan hasil prediksi/rekomendasi secara real-time. |
| **Dokumentasi & GitHub Repository** | 10% | README informatif, instruksi instalasi jelas, struktur folder rapi, dan mencantumkan tautan demo aplikasi. |

---

## 🆘 5. Strategi Menghadapi Error (Debugging Guide)

Ketika Anda menemui error saat menjalankan kode di Colab:
1. **Tarik Nafas & Baca Baris Terakhir**: Pesan error Python selalu meletakkan penyebab utama di baris paling bawah.
2. **Cek Tipe Data & Dimensi**: Gunakan `df.info()`, `df.dtypes`, dan `df.shape`. Sebagian besar error terjadi karena kolom salah tipe (misal string yang terbaca numerik) atau dimensi array tidak cocok.
3. **Cari Jawaban dengan Tepat**: Salin teks pesan error baris terakhir ke mesin pencari atau forum Stack Overflow.
4. **Gunakan Bantuan AI secara Bijak**: Tanyakan kepada asisten AI dengan menyertakan potongan kode dan pesan error lengkap agar mendapat penjelasan penyebabnya, bukan sekadar jawaban instan.
