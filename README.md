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

```bash
pip install -r requirements.txt
```

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
