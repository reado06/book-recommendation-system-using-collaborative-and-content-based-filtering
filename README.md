# 📚 Sistem Rekomendasi Perpustakaan

Book Recommendation System using **Hybrid Recommender** (Collaborative + Content-Based Filtering).

## 📋 Deskripsi

Sistem ini merekomendasikan buku sesuai minat dan histori peminjaman mahasiswa menggunakan dua pendekatan:

1. **Content-Based Filtering** — Merekomendasikan buku berdasarkan kesamaan penulis menggunakan TF-IDF Vectorizer dan Cosine Similarity.
2. **Collaborative Filtering** — Merekomendasikan buku berdasarkan pola rating pengguna lain menggunakan algoritma SVD (Surprise).
3. **Hybrid Approach** — Menggabungkan skor kedua metode dengan weighted average.

## 📁 Dataset

Dataset menggunakan [Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) dari Kaggle:

```
Dataset/
├── Books.csv     # 271.360 buku (ISBN, judul, penulis, tahun, penerbit)
├── Ratings.csv   # 1.149.780 rating (User-ID, ISBN, Book-Rating 0-10)
└── Users.csv     # 278.858 user (User-ID, Location, Age)
```

## 🛠️ Tech Stack

- **Python** — Bahasa pemrograman utama
- **Surprise** — Library untuk Collaborative Filtering (SVD)
- **scikit-learn** — TF-IDF Vectorizer, Cosine Similarity
- **Flask** — Web framework untuk halaman rekomendasi
- **SQLite** — Database
- **pandas, numpy, matplotlib, seaborn** — Data processing & visualisasi

## 🚀 Cara Menjalankan

### 1. Install Dependencies

**⚠️ PENTING (Khusus Pengguna Windows)**
Library `scikit-surprise` tidak memiliki *pre-built wheel* untuk Python versi terbaru di Windows, sehingga membutuhkan *C++ compiler* untuk diinstal. Terdapat dua opsi yang bisa dilakukan sebelum menginstall dependencies:

**Opsi 1: Microsoft C++ Build Tools (Sudah Diuji & Berhasil)**
1. Download **[Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)**.
2. Jalankan installer dan centang pilihan **"Desktop development with C++"**.
   *(Perhatian: Ukuran download file sekitar 2 GB dan memakan penyimpanan sekitar 6-7 GB setelah di-extract).*
3. Setelah proses instalasi selesai, **restart komputer/laptop** Anda.

**Opsi 2: Miniconda / Anaconda (Alternatif - Belum Diuji)**
Jika tidak ingin mendownload file sebesar 6 GB, alternatifnya adalah menggunakan environment Conda:
```bash
conda install -c conda-forge scikit-surprise
```

Setelah menyelesaikan salah satu prerequisite di atas (atau jika Anda menggunakan Linux/Mac), jalankan instalasi *requirements* utama:

```bash
pip install -r requirements.txt
```

*(Catatan: File `requirements.txt` ini sudah disesuaikan untuk menggunakan `numpy<2` guna menghindari error "compiled using NumPy 1.x cannot be run in NumPy 2.x").*

### 2. Jalankan Notebook

Buka `notebook.ipynb` di Jupyter Notebook/Lab atau VS Code, lalu jalankan semua cell dari awal sampai akhir. Notebook ini akan:

- Melakukan EDA dan preprocessing data
- Melatih model Content-Based dan Collaborative Filtering
- Mengevaluasi model (NDCG@10)
- Meng-export model ke folder `models/`

### 3. Jalankan Web App

```bash
python run.py
```

Buka browser dan akses `http://127.0.0.1:5000`

## 📊 Metrik Evaluasi

| Metrik  | Target  | Hasil  |
| ------- | ------- | ------ |
| NDCG@10 | >= 0.75 | 0.9718 |
| RMSE    | -       | 1.5920 |
| MAE     | -       | 1.2241 |

## 📂 Struktur Project

```
Sistem_Rekomendasi_Perpustakaan/
├── Dataset/              # Dataset CSV dari Kaggle
├── notebook.ipynb        # Notebook lengkap (EDA → Model → Evaluasi)
├── models/               # Model yang sudah di-train (pickle)
├── app/                  # Flask Web App
│   ├── templates/        # HTML templates
│   ├── static/css/       # Styling
│   ├── recommender.py    # Hybrid recommendation engine
│   └── routes.py         # Flask routes
├── run.py                # Entry point Flask
├── requirements.txt      # Dependencies
└── README.md             # Dokumentasi
```

## 📝 Referensi

- [Juwono136 - Book Recommendation System](https://github.com/Juwono136/book-recommendation-system-using-content-based-filtering-and-collaborative-filtering)
- [Book Recommendation Dataset - Kaggle](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)
