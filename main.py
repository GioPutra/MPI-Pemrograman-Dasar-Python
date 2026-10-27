
import tkinter as tk
from tkinter import messagebox

# Membuat jendela utama MPI
jendela = tk.Tk()
jendela.title("MPI Pemrograman Dasar Python")
jendela.geometry("700x450")
jendela.configure(bg="#f0f4f8")

# Judul aplikasi
judul = tk.Label(
    jendela,
    text="MPI PEMROGRAMAN DASAR PYTHON",
    font=("Arial", 20, "bold"),
    bg="#f0f4f8",
    fg="#17365D"
)
judul.pack(pady=40)

# Deskripsi aplikasi
deskripsi = tk.Label(
    jendela,
    text="Media Pembelajaran Interaktif untuk Belajar Python",
    font=("Arial", 12),
    bg="#f0f4f8"
)
deskripsi.pack(pady=10)

# Tombol mulai
def mulai_belajar():
    messagebox.showinfo(
        "MPI Pemrograman Dasar",
        "Selamat datang! Mari mulai belajar Python."
    )

tombol = tk.Button(
    jendela,
    text="MULAI BELAJAR",
    font=("Arial", 12, "bold"),
    bg="#17365D",
    fg="white",
    padx=25,
    pady=12,
    command=mulai_belajar
)
tombol.pack(pady=30)

# Menjalankan aplikasi
jendela.mainloop()
