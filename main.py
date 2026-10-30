
import tkinter as tk
from tkinter import messagebox

# Konfigurasi aplikasi
JUDUL_APLIKASI = "MPI Pemrograman Dasar Python"
WARNA_BACKGROUND = "#f0f4f8"
WARNA_UTAMA = "#17365D"


# Membuat jendela utama aplikasi
def buat_jendela_utama():
    jendela = tk.Tk()
    jendela.title(JUDUL_APLIKASI)
    jendela.geometry("700x500")
    jendela.configure(bg=WARNA_BACKGROUND)

    # Judul aplikasi
    judul = tk.Label(
        jendela,
        text="MPI PEMROGRAMAN DASAR PYTHON",
        font=("Arial", 20, "bold"),
        bg=WARNA_BACKGROUND,
        fg=WARNA_UTAMA
    )
    judul.pack(pady=(40, 10))

    # Deskripsi aplikasi
    deskripsi = tk.Label(
        jendela,
        text="Media Pembelajaran Interaktif untuk Belajar Python",
        font=("Arial", 11),
        bg=WARNA_BACKGROUND
    )
    deskripsi.pack(pady=(0, 25))

    # Fungsi menu materi
    def buka_materi():
        halaman_materi = tk.Toplevel(jendela)
        halaman_materi.title("Materi Pembelajaran")
        halaman_materi.geometry("600x450")
        halaman_materi.configure(bg=WARNA_BACKGROUND)

        judul_materi = tk.Label(
            halaman_materi,
            text="MATERI PEMBELAJARAN PYTHON",
            font=("Arial", 18, "bold"),
            bg=WARNA_BACKGROUND,
            fg=WARNA_UTAMA
        )
        judul_materi.pack(pady=30)

        deskripsi_materi = tk.Label(
            halaman_materi,
            text="Pilih materi yang ingin kamu pelajari:",
            font=("Arial", 11),
            bg=WARNA_BACKGROUND
        )
        deskripsi_materi.pack(pady=10)

        # Daftar materi
        daftar_materi = [
            "1. Pengenalan Python",
            "2. Variabel dalam Python",
            "3. Tipe Data Python",
            "4. Operator Dasar Python"
        ]

        # Menampilkan daftar materi
        for materi in daftar_materi:
            label_materi = tk.Label(
                halaman_materi,
                text=materi,
                font=("Arial", 12),
                bg="white",
                fg=WARNA_UTAMA,
                width=35,
                pady=10
            )
            label_materi.pack(pady=6)

    # Fungsi menu kuis
    def buka_kuis():
        messagebox.showinfo(
            "Kuis",
            "Menu kuis akan segera tersedia."
        )

    # Fungsi menu tentang aplikasi
    def buka_tentang():
        messagebox.showinfo(
            "Tentang Aplikasi",
            "MPI Pemrograman Dasar Python adalah aplikasi "
            "pembelajaran interaktif untuk mempelajari dasar Python."
        )

    # Fungsi keluar aplikasi
    def keluar_aplikasi():
        konfirmasi = messagebox.askyesno(
            "Keluar",
            "Apakah kamu yakin ingin keluar dari aplikasi?"
        )
        if konfirmasi:
            jendela.destroy()

    # Tombol menu utama
    daftar_menu = [
        ("MATERI PEMBELAJARAN", buka_materi),
        ("KUIS", buka_kuis),
        ("TENTANG APLIKASI", buka_tentang),
        ("KELUAR", keluar_aplikasi)
    ]

    for teks, fungsi in daftar_menu:
        tombol = tk.Button(
            jendela,
            text=teks,
            font=("Arial", 11, "bold"),
            bg=WARNA_UTAMA,
            fg="white",
            width=28,
            pady=9,
            command=fungsi
        )
        tombol.pack(pady=6)

    return jendela


# Menjalankan aplikasi
if __name__ == "__main__":
    aplikasi = buat_jendela_utama()
    aplikasi.mainloop()
