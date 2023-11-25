import tkinter as tk
from tkinter import ttk
import sqlite3

def hitung_prediksi():
    nama_siswa = entry_nama.get()
    nilai_biologi = int(entry_biologi.get())
    nilai_fisika = int(entry_fisika.get())
    nilai_inggris = int(entry_inggris.get())

    #Logika prediksi prodi
    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prediksi_prodi = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prediksi_prodi = "Teknik"
    elif nilai_inggris > nilai_biologi and nilai_inggris > nilai_fisika:
        prediksi_prodi =   "Bahasa"
    else:
        prediksi_prodi = "Tidak Terprediksi"

    label_hasil.config(text=f"Hasil Prediksi: {prediksi_prodi}")

    #Simpan data ke DB
    conn = sqlite3.connect('prediksi_prodi.db')
    cursor = conn.cursor()

    #Membuat table jika belum ada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            prediksi_fakultas TEXT
        )
    ''')
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi_prodi))
    conn.commit()
    conn.close()

#Membuat GUI
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

#Judul Aplikasi
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=('Times New Roman', 22))
label_judul.grid(row=0, column=0, columnspan=4, pady=10)

#Input nilai mata pelajaran
label_nama = tk.Label(root, text="Nama Siswa   :", font=('Times New Roman', 16))
label_nama.grid(row=1, column=0, pady=5)
entry_nama = tk.Entry(root)
entry_nama.grid(row=1, column=1, pady=5)

label_biologi = tk.Label(root, text="Nilai Biologi :", font=('Times New Roman', 16))
label_biologi.grid(row=2, column=0, pady=5)
entry_biologi = tk.Entry(root)
entry_biologi.grid(row=2, column=1, pady=5)

label_fisika = tk.Label(root, text="Nilai Fisika   :", font=('Times New Roman', 16))
label_fisika.grid(row=3, column=0, pady=5)
entry_fisika = tk.Entry(root)
entry_fisika.grid(row=3, column=1, pady=5)

label_inggris = tk.Label(root, text="Nilai Inggris  :", font=('Times New Roman', 16))
label_inggris.grid(row=4, column=0, pady=5)
entry_inggris = tk.Entry(root)
entry_inggris.grid(row=4, column=1, pady=5)

#Tombol untuk hasil prediksi
button_prediksi = tk.Button(root, text="Hasil Prediksi", command=hitung_prediksi)
button_prediksi.grid(row=5, column=0, columnspan=2, pady=10)

#Label hasil prediksi
label_hasil = tk.Label(root, text="Hasil Prediksi: ")
label_hasil.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()