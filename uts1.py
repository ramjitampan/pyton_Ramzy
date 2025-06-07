import tkinter as tk
from tkinter import messagebox

def ubah_nilai_ke_huruf(skor):
    if skor >= 85:
        return "A", 4.0, "Dengan pujian"
    elif skor >= 80:
        return "A-", 3.6, "Sangat baik sekali"
    elif skor >= 75:
        return "B+", 3.3, "Baik sekali"
    elif skor >= 70:
        return "B", 3.0, "Baik"
    elif skor >= 65:
        return "B-", 2.6, "Cukup Baik"
    elif skor >= 60:
        return "C+", 2.3, "Lebih dari cukup"
    elif skor >= 55:
        return "C", 2.0, "Cukup"
    elif skor >= 50:
        return "C-", 1.6, "Kurang cukup"
    elif skor >= 40:
        return "D", 1.0, "Kurang"
    else:
        return "E", 0.0, "Kamu GAGAL"

def hitung_nilai():
    try:
        tugas = float(entry_tugas.get())
        hadir = float(entry_kehadiran.get())
        uts = float(entry_uts.get())
        uas = float(entry_uas.get())

        nilai_akhir = (tugas * 0.3) + (hadir * 0.1) + (uts * 0.25) + (uas * 0.35)
        huruf, mutu, kategori = ubah_nilai_ke_huruf(nilai_akhir)

        hasil = (
            f"Nama: {entry_nama.get()}\n"
            f"Prodi: {entry_prodi.get()}\n"
            f"Nilai Akhir: {nilai_akhir:.2f}\n"
            f"Huruf: {huruf}\n"
            f"Mutu: {mutu}\n"
            f"Kategori: {kategori}\n"
        )

        if mutu >= 3.0:
            hasil += "Rekomendasi: Keren pertahankan jangan sampai turun, Semangat!"
        elif mutu >= 2.0:
            hasil += "Rekomendasi: Aduhai tidak papa masik ada yang lain tetap semangatt."
        else:
            hasil += "Rekomendasi: inimah skill isue, Segera konsultasi dengan dosen pembimbing."

        messagebox.showinfo("Hasil Penilaian", hasil)
    except ValueError:
        messagebox.showerror("Error", "Harap masukkan nilai numerik yang valid.")

root = tk.Tk()  
root.title("Sistem Penilaian Mahasiswa")

tk.Label(root, text="Nama Mahasiswa").grid(row=0, column=0, sticky="w")
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1)

tk.Label(root, text="Program Studi").grid(row=1, column=0, sticky="w")
entry_prodi = tk.Entry(root)
entry_prodi.grid(row=1, column=1)

tk.Label(root, text="Nilai Tugas").grid(row=2, column=0, sticky="w")
entry_tugas = tk.Entry(root)
entry_tugas.grid(row=2, column=1)

tk.Label(root, text="Nilai Kehadiran").grid(row=3, column=0, sticky="w")
entry_kehadiran = tk.Entry(root)
entry_kehadiran.grid(row=3, column=1)

tk.Label(root, text="Nilai UTS").grid(row=4, column=0, sticky="w")
entry_uts = tk.Entry(root)
entry_uts.grid(row=4, column=1)

tk.Label(root, text="Nilai UAS").grid(row=5, column=0, sticky="w")
entry_uas = tk.Entry(root)
entry_uas.grid(row=5, column=1)

btn_hitung = tk.Button(root, text="Hitung Nilai", command=hitung_nilai)
btn_hitung.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
