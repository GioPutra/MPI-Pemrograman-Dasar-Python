
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
    jendela.geometry("700x450")
    jendela.configure(bg=WARNA_BACKGROUND)

    # Judul aplikasi
    judul = tk.Label(
        jendela,
        text="MPI PEMROGRAMAN DASAR PYTHON",
        font=("Arial", 20, "bold"),
        bg=WARNA_BACKGROUND,
        fg=WARNA_UTAMA
    )
    judul.pack(pady=40)

    # Deskripsi aplikasi
    deskripsi = tk.Label(
        jendela,
        text="Media Pembelajaran Interaktif untuk Belajar Python",
        font=("Arial", 12),
        bg=WARNA_BACKGROUND
    )
    deskripsi.pack(pady=10)

    # Fungsi tombol mulai belajar
    def mulai_belajar():
        messagebox.showinfo(
            "MPI Pemrograman Dasar",
            "Selamat datang! Mari mulai belajar Python."
        )

    # Tombol mulai belajar
    tombol = tk.Button(
        jendela,
        text="MULAI BELAJAR",
        font=("Arial", 12, "bold"),
        bg=WARNA_UTAMA,
        fg="white",
        padx=25,
        pady=12,
        command=mulai_belajar
    )
    tombol.pack(pady=30)

    return jendela


# Menjalankan aplikasi
if __name__ == "__main__":
    aplikasi = buat_jendela_utama()
    aplikasi.mainloop()
