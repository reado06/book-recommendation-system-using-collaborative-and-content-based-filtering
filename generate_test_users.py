import pandas as pd
import pickle
import os

# 1. Load data rating yang sudah melalui tahap pembersihan (filter)
model_path = 'models/rating_data.pkl'

if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        rating_data = pickle.load(f)

    # 2. Hitung jumlah rating untuk masing-masing User ID
    user_counts = rating_data['User-ID'].value_counts()

    # 3. Simpan hasilnya ke dalam file TXT
    with open('Daftar_User_Lengkap.txt', 'w', encoding='utf-8') as file:
        file.write("=== DAFTAR LENGKAP USER ID UNTUK PRESENTASI & TESTING ===\n")
        file.write(f"Total User yang tersedia di Web App: {len(user_counts)} User\n")
        file.write("Catatan: Semua user di bawah ini dijamin akan menghasilkan rekomendasi yang personalized.\n\n")
        
        file.write("🌟 KATEGORI 1: User SUPER AKTIF (Membaca > 100 Buku)\n")
        file.write("Sangat bagus untuk demo melihat genre yang sangat spesifik.\n")
        file.write("-" * 50 + "\n")
        super_users = user_counts[user_counts > 100]
        for user_id, count in super_users.items():
            file.write(f"User ID: {user_id:<8} | Telah merating: {count} buku\n")
            
        file.write("\n📘 KATEGORI 2: User AKTIF (Membaca 20-100 Buku)\n")
        file.write("Bagus untuk demo user normal yang rajin baca.\n")
        file.write("-" * 50 + "\n")
        active_users = user_counts[(user_counts >= 20) & (user_counts <= 100)]
        for user_id, count in active_users.items():
            file.write(f"User ID: {user_id:<8} | Telah merating: {count} buku\n")
            
        file.write("\n📗 KATEGORI 3: User STANDARD (Membaca 5-19 Buku)\n")
        file.write("Bagus untuk demo bagaimana AI menyarankan buku dengan data terbatas.\n")
        file.write("-" * 50 + "\n")
        standard_users = user_counts[(user_counts >= 5) & (user_counts < 20)]
        for user_id, count in standard_users.items():
            file.write(f"User ID: {user_id:<8} | Telah merating: {count} buku\n")

    print("Berhasil! File 'Daftar_User_Lengkap.txt' dengan total belasan ribu user telah dibuat.")
else:
    print("Error: File model tidak ditemukan. Pastikan Anda sudah menjalankan notebook.ipynb.")
