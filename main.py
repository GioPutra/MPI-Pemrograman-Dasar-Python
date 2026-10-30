
import tkinter as tk
from tkinter import messagebox

# Konfigurasi aplikasi
JUDUL_APLIKASI = "MPI Pemrograman Dasar Python"
WARNA_BACKGROUND = "#f0f4f8"
WARNA_UTAMA = "#17365D"


# Data materi pembelajaran
DATA_MATERI = [
    {
        "judul": "1. Pengenalan Python",
        "isi": (
            "Python adalah bahasa pemrograman tingkat tinggi "
            "yang mudah dipelajari dan memiliki sintaks sederhana.\n\n"
            "Python dapat digunakan untuk membuat aplikasi desktop, "
            "website, mengolah data, kecerdasan buatan, dan otomatisasi.\n\n"
            "Python dikembangkan oleh Guido van Rossum dan pertama "
            "kali dirilis pada tahun 1991."
        ),
        "contoh": 'print("Halo, Dunia!")'
    },
    {
        "judul": "2. Variabel dalam Python",
        "isi": (
            "Variabel adalah tempat untuk menyimpan data di dalam "
            "program.\n\n"
            "Variabel dapat digunakan untuk menyimpan nama, umur, "
            "alamat, dan berbagai informasi lainnya.\n\n"
            "Nama variabel tidak boleh diawali angka dan tidak boleh "
            "menggunakan spasi."
        ),
        "contoh": 'nama = "Gio"\numur = 17\nprint(nama)\nprint(umur)'
    },
    {
        "judul": "3. Tipe Data Python",
        "isi": (
            "Tipe data merupakan jenis nilai yang disimpan dalam "
            "variabel.\n\n"
            "Beberapa tipe data dasar Python adalah:\n\n"
            "1. Integer: bilangan bulat.\n"
            "2. Float: bilangan desimal.\n"
            "3. String: kumpulan karakter atau teks.\n"
            "4. Boolean: nilai True atau False."
        ),
        "contoh": (
            'umur = 17\n'
            'tinggi = 165.5\n'
            'nama = "Gio"\n'
            'aktif = True\n\n'
            'print(type(umur))\n'
            'print(type(tinggi))\n'
            'print(type(nama))\n'
            'print(type(aktif))'
        )
    },
    {
        "judul": "4. Operator Dasar Python",
        "isi": (
            "Operator adalah simbol yang digunakan untuk melakukan "
            "operasi terhadap data.\n\n"
            "Operator aritmatika dasar meliputi:\n\n"
            "+ : Penjumlahan\n"
            "- : Pengurangan\n"
            "* : Perkalian\n"
            "/ : Pembagian\n"
            "% : Modulus atau sisa bagi"
        ),
        "contoh": (
            'angka1 = 10\n'
            'angka2 = 5\n\n'
            'print(angka1 + angka2)\n'
            'print(angka1 - angka2)\n'
            'print(angka1 * angka2)\n'
            'print(angka1 / angka2)'
        )
    }
]


# Membuat jendela utama
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

    # Fungsi menampilkan isi materi
    def tampilkan_materi(materi):
        halaman = tk.Toplevel(jendela)
        halaman.title(materi["judul"])
        halaman.geometry("650x550")
        halaman.configure(bg=WARNA_BACKGROUND)

        judul_materi = tk.Label(
            halaman,
            text=materi["judul"],
            font=("Arial", 18, "bold"),
            bg=WARNA_BACKGROUND,
            fg=WARNA_UTAMA
        )
        judul_materi.pack(pady=20)

        isi_materi = tk.Label(
            halaman,
            text=materi["isi"],
            font=("Arial", 11),
            bg=WARNA_BACKGROUND,
            justify="left",
            wraplength=570
        )
        isi_materi.pack(padx=30, pady=10, anchor="w")

        label_contoh = tk.Label(
            halaman,
            text="Contoh Kode Python:",
            font=("Arial", 12, "bold"),
            bg=WARNA_BACKGROUND,
            fg=WARNA_UTAMA
        )
        label_contoh.pack(pady=(15, 5))

        kotak_kode = tk.Text(
            halaman,
            height=8,
            width=65,
            font=("Consolas", 11),
            bg="#e2e8f0",
            fg="#172554",
            relief="flat",
            padx=10,
            pady=10
        )
        kotak_kode.pack(padx=25, pady=5)

        kotak_kode.insert("1.0", materi["contoh"])
        kotak_kode.configure(state="disabled")

    # Fungsi membuka halaman materi
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
        judul_materi.pack(pady=25)

        deskripsi_materi = tk.Label(
            halaman_materi,
            text="Pilih materi yang ingin kamu pelajari:",
            font=("Arial", 11),
            bg=WARNA_BACKGROUND
        )
        deskripsi_materi.pack(pady=10)

        for materi in DATA_MATERI:
            tombol = tk.Button(
                halaman_materi,
                text=materi["judul"],
                font=("Arial", 12),
                bg="white",
                fg=WARNA_UTAMA,
                width=35,
                pady=10,
                command=lambda m=materi: tampilkan_materi(m)
            )
            tombol.pack(pady=6)

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

    # Daftar tombol menu utama
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
