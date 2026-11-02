import tkinter as tk
from tkinter import messagebox
import random

# Konfigurasi aplikasi
JUDUL_APLIKASI = "MPI Pemrograman Dasar Python"
WARNA_BACKGROUND = "#f0f4f8"
WARNA_UTAMA = "#17365D"
JUMLAH_SOAL_KUIS = 10

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
            "Variabel adalah tempat untuk menyimpan data di dalam program.\n\n"
            "Variabel dapat digunakan untuk menyimpan nama, umur, alamat, "
            "dan berbagai informasi lainnya.\n\n"
            "Nama variabel tidak boleh diawali angka dan tidak boleh "
            "menggunakan spasi."
        ),
        "contoh": 'nama = "Gio"\numur = 17\nprint(nama)\nprint(umur)'
    },
    {
        "judul": "3. Tipe Data Python",
        "isi": (
            "Tipe data merupakan jenis nilai yang disimpan dalam variabel.\n\n"
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
            "% : Modulus atau sisa bagi\n"
            "// : Pembagian bulat\n"
            "** : Perpangkatan"
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


def buat_soal(soal, pilihan, jawaban, pembahasan=""):
    """Membuat satu data soal beserta pembahasannya."""
    return {
        "soal": soal,
        "pilihan": pilihan,
        "jawaban": jawaban,
        "pembahasan": pembahasan
    }


# Setiap tingkat memiliki 20 soal. Total tetap 60 soal.
BANK_SOAL = {
    "Mudah": [
        buat_soal("Python termasuk jenis ...", ["Bahasa pemrograman", "Perangkat keras", "Sistem operasi", "Jaringan komputer"], 0, "Python adalah bahasa pemrograman, yaitu bahasa yang digunakan untuk memberikan instruksi kepada komputer."),
        buat_soal("Siapa pengembang Python?", ["Bill Gates", "Guido van Rossum", "Steve Jobs", "Mark Zuckerberg"], 1, "Python dikembangkan oleh Guido van Rossum dan pertama kali dirilis pada tahun 1991."),
        buat_soal("Pada tahun berapa Python pertama kali dirilis?", ["1980", "1985", "1991", "2000"], 2, "Python pertama kali dirilis pada tahun 1991."),
        buat_soal("Perintah untuk menampilkan teks adalah ...", ["input()", "show()", "print()", "write()"], 2, "Fungsi print() digunakan untuk menampilkan teks atau nilai ke layar."),
        buat_soal("Variabel digunakan untuk ...", ["Menyimpan data", "Mematikan komputer", "Menghapus aplikasi", "Menggambar"], 0, "Variabel merupakan tempat untuk menyimpan data agar dapat digunakan kembali dalam program."),
        buat_soal("Manakah nama variabel yang benar?", ["2nama", "nama siswa", "nama_siswa", "nama-siswa"], 2, "nama_siswa valid karena tidak diawali angka dan tidak mengandung spasi atau tanda hubung."),
        buat_soal("Tipe data untuk bilangan bulat adalah ...", ["String", "Integer", "Float", "Boolean"], 1, "Integer (int) digunakan untuk menyimpan bilangan bulat, misalnya 17 atau 25."),
        buat_soal("Tipe data untuk teks adalah ...", ["String", "Integer", "Float", "Boolean"], 0, "String (str) digunakan untuk menyimpan teks atau kumpulan karakter."),
        buat_soal("True dan False termasuk tipe data ...", ["String", "Integer", "Boolean", "Float"], 2, "Boolean (bool) memiliki dua nilai, yaitu True dan False."),
        buat_soal("Tipe data untuk angka desimal adalah ...", ["Integer", "String", "Float", "Boolean"], 2, "Float digunakan untuk menyimpan angka yang memiliki bagian desimal, misalnya 3.5."),
        buat_soal("Simbol penjumlahan dalam Python adalah ...", ["+", "-", "*", "/"], 0, "Operator + digunakan untuk melakukan penjumlahan."),
        buat_soal("Simbol pengurangan dalam Python adalah ...", ["+", "-", "*", "/"], 1, "Operator - digunakan untuk melakukan pengurangan."),
        buat_soal("Simbol perkalian dalam Python adalah ...", ["+", "-", "*", "/"], 2, "Operator * digunakan untuk melakukan perkalian."),
        buat_soal("Simbol pembagian dalam Python adalah ...", ["+", "-", "*", "/"], 3, "Operator / digunakan untuk melakukan pembagian dan menghasilkan nilai bertipe float."),
        buat_soal("Apa hasil dari 4 + 3?", ["6", "7", "8", "9"], 1, "4 ditambah 3 sama dengan 7."),
        buat_soal("Apa hasil dari 9 - 5?", ["3", "4", "5", "6"], 1, "9 dikurangi 5 sama dengan 4."),
        buat_soal("Apa hasil dari 3 * 4?", ["7", "10", "12", "14"], 2, "3 dikalikan 4 sama dengan 12."),
        buat_soal('Pada kode nama = "Rina", nilai "Rina" bertipe ...', ["Integer", "Float", "String", "Boolean"], 2, "Nilai Rina ditulis di dalam tanda kutip sehingga merupakan data teks bertipe String."),
        buat_soal("Manakah nilai Boolean?", ['"Benar"', "25", "3.5", "True"], 3, "True merupakan salah satu nilai Boolean. Nilai Boolean lainnya adalah False."),
        buat_soal("Fungsi type() digunakan untuk mengetahui ...", ["Nama file", "Tipe data", "Warna teks", "Ukuran layar"], 1, "Fungsi type() digunakan untuk mengetahui tipe data dari suatu nilai atau variabel.")
    ],
    "Menengah": [
        buat_soal("Apa keluaran dari print(10 + 5)?", ["10", "15", "105", "5"], 1, "Operasi 10 + 5 menghasilkan 15, lalu print() menampilkannya."),
        buat_soal("Apa keluaran dari print(12 - 7)?", ["4", "5", "6", "19"], 1, "12 dikurangi 7 menghasilkan 5."),
        buat_soal("Apa keluaran dari print(6 * 3)?", ["9", "12", "18", "21"], 2, "6 dikalikan 3 menghasilkan 18."),
        buat_soal("Apa hasil dari 20 / 4 di Python?", ["5", "5.0", "16", "80"], 1, "Operator / melakukan pembagian biasa. Di Python, hasil 20 / 4 adalah 5.0 bertipe float."),
        buat_soal("Apa hasil dari 17 % 5?", ["2", "3", "5", "12"], 0, "Operator % menghasilkan sisa pembagian. 17 dibagi 5 bersisa 2."),
        buat_soal('Apa keluaran dari nama = "Dina"; print(nama)?', ["nama", "Dina", "print", "Error"], 1, "Teks Dina disimpan ke variabel nama. print(nama) menampilkan isi variabel, yaitu Dina."),
        buat_soal("Manakah penamaan variabel yang valid?", ["nilai akhir", "nilai-akhir", "nilai_akhir", "3nilai"], 2, "nilai_akhir valid karena memakai garis bawah dan tidak diawali angka."),
        buat_soal("Apa tipe data dari nilai = 12.75?", ["Integer", "Float", "String", "Boolean"], 1, "12.75 merupakan bilangan desimal sehingga tipe datanya Float."),
        buat_soal('Apa tipe data dari kode status = "True"?', ["Boolean", "Integer", "String", "Float"], 2, 'True yang berada di dalam tanda kutip merupakan teks, sehingga bertipe String.'),
        buat_soal("Apa keluaran dari print(type(25))?", ["<class 'str'>", "<class 'int'>", "<class 'float'>", "<class 'bool'>"], 1, "Angka 25 adalah bilangan bulat. type(25) menunjukkan kelas int."),
        buat_soal("Apa keluaran dari print(8 + 2 * 3)?", ["30", "14", "24", "13"], 1, "Perkalian dikerjakan lebih dahulu: 2 * 3 = 6, kemudian 8 + 6 = 14."),
        buat_soal("Jika a = 15 dan b = 4, berapa hasil a % b?", ["2", "3", "4", "3.75"], 1, "15 dibagi 4 menghasilkan sisa 3, sehingga a % b bernilai 3."),
        buat_soal("Jika umur = 16, tipe data umur adalah ...", ["String", "Float", "Integer", "Boolean"], 2, "Nilai 16 adalah bilangan bulat sehingga bertipe Integer."),
        buat_soal('Manakah kode untuk menyimpan teks "Halo" ke variabel pesan?', ['pesan = Halo', 'pesan = "Halo"', '"Halo" = pesan', 'pesan == "Halo"'], 1, 'Teks harus ditulis di dalam tanda kutip. Tanda = digunakan untuk memberikan nilai kepada variabel.'),
        buat_soal("Apa keluaran dari x = 5; x = x + 2; print(x)?", ["5", "2", "7", "10"], 2, "Nilai awal x adalah 5. Kemudian x diperbarui menjadi 5 + 2, yaitu 7."),
        buat_soal("Operator % digunakan untuk memperoleh ...", ["Hasil kali", "Sisa pembagian", "Hasil penjumlahan", "Hasil pembagian desimal"], 1, "Operator modulus (%) menghasilkan sisa dari suatu operasi pembagian."),
        buat_soal("Manakah contoh nilai float?", ["8", '"8.5"', "8.5", "False"], 2, "8.5 adalah angka desimal yang tidak diapit tanda kutip, sehingga bertipe float."),
        buat_soal("Apa keluaran dari print(18 / 3)?", ["6", "6.0", "15", "54"], 1, "Pembagian dengan operator / menghasilkan float. Jadi 18 / 3 menghasilkan 6.0."),
        buat_soal("Apa keluaran dari print(7 * 2 - 4)?", ["6", "10", "18", "24"], 1, "Perkalian dikerjakan lebih dahulu: 7 * 2 = 14, lalu 14 - 4 = 10."),
        buat_soal("Mengapa nama variabel tidak boleh diawali angka?", ["Karena melanggar aturan penamaan", "Karena harus selalu huruf besar", "Karena variabel hanya untuk teks", "Karena angka tidak bisa dihitung"], 0, "Dalam aturan penamaan identifier Python, nama variabel tidak boleh diawali angka.")
    ],
    "Sulit": [
        buat_soal("Perhatikan a = 8; b = 3; print(a // b). Apa hasilnya?", ["2", "2.66", "3", "5"], 0, "Operator // melakukan pembagian bulat. 8 dibagi 3 adalah 2.66..., sehingga hasil pembagian bulatnya 2."),
        buat_soal("Perhatikan x = 5; x = x * 2; x = x + 1. Nilai akhir x adalah ...", ["10", "11", "12", "15"], 1, "Nilai x mula-mula 5, kemudian menjadi 5 * 2 = 10, lalu 10 + 1 = 11."),
        buat_soal("Apa keluaran dari print(2 + 3 * 4 - 5)?", ["9", "15", "17", "20"], 0, "Perkalian dikerjakan lebih dahulu: 3 * 4 = 12. Selanjutnya 2 + 12 - 5 = 9."),
        buat_soal("Jika a = 23 dan b = 6, nilai a % b adalah ...", ["3", "4", "5", "6"], 2, "23 dibagi 6 menghasilkan 3 dengan sisa 5. Jadi 23 % 6 = 5."),
        buat_soal("Apa keluaran dari print(30 / (2 + 3))?", ["5", "6.0", "10", "15"], 1, "Kerjakan tanda kurung terlebih dahulu: 2 + 3 = 5. Kemudian 30 / 5 = 6.0."),
        buat_soal('Diberikan data = "10". Apa cara tepat mengubahnya menjadi bilangan bulat?', ["str(data)", "float(data)", "int(data)", "bool(data)"], 2, "Fungsi int() mengonversi teks angka seperti '10' menjadi bilangan bulat 10."),
        buat_soal("Apa tipe data hasil dari operasi 9 / 3 pada Python?", ["Integer", "Float", "String", "Boolean"], 1, "Operator pembagian biasa / menghasilkan tipe float di Python, sehingga 9 / 3 menghasilkan 3.0."),
        buat_soal("Apa keluaran dari x = 4; y = 2; print(x ** y)?", ["6", "8", "16", "42"], 2, "Operator ** berarti perpangkatan. 4 ** 2 berarti 4 pangkat 2, hasilnya 16."),
        buat_soal("Apa keluaran dari print(5 + 2 ** 3)?", ["13", "21", "49", "64"], 0, "Perpangkatan dikerjakan lebih dahulu: 2 ** 3 = 8, kemudian 5 + 8 = 13."),
        buat_soal("Jika nilai = 14, kemudian nilai = nilai - 6, hasil akhirnya ...", ["6", "7", "8", "20"], 2, "Nilai awal 14 dikurangi 6, sehingga nilai akhirnya 8."),
        buat_soal("Apa keluaran dari print(19 // 4)?", ["3", "4", "4.75", "5"], 1, "19 dibagi 4 adalah 4.75. Operator // mengambil hasil pembagian bulat, yaitu 4."),
        buat_soal("Apa keluaran dari print(19 % 4 + 2)?", ["3", "5", "6", "7"], 1, "19 % 4 menghasilkan sisa 3. Kemudian 3 + 2 = 5."),
        buat_soal('Variabel x = "7" dan y = "2". Apa hasil print(x + y)?', ["9", "72", "14", "Error"], 1, "Kedua nilai merupakan String. Operator + menggabungkan teks, sehingga hasilnya '72'."),
        buat_soal("Apa keluaran dari print(10 - 2 * 3 ** 2)?", ["-8", "24", "64", "72"], 0, "Urutan operasi: 3 ** 2 = 9, lalu 2 * 9 = 18, kemudian 10 - 18 = -8."),
        buat_soal("Jika a = 10 dan b = 3, ekspresi untuk mendapatkan hasil 3 adalah ...", ["a / b", "a // b", "a % b", "a * b"], 1, "10 % 3 menghasilkan sisa pembagian 1, bukan 3. Catatan: pada soal ini opsi yang benar seharusnya diperbaiki; ekspresi a // b menghasilkan 3."),
        buat_soal("Apa keluaran dari x = 3.0; print(type(x))?", ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'bool'>"], 2, "Nilai 3.0 ditulis dengan bagian desimal, sehingga Python mengenalinya sebagai float."),
        buat_soal("Manakah pernyataan yang benar tentang String?", ["Selalu berupa angka bulat", "Digunakan untuk menyimpan teks", "Hanya berisi True atau False", "Tidak dapat disimpan dalam variabel"], 1, "String digunakan untuk menyimpan teks, misalnya nama, alamat, atau kalimat."),
        buat_soal("Apa keluaran dari print((8 + 4) / 3)?", ["4", "4.0", "12", "36"], 1, "Kerjakan tanda kurung: 8 + 4 = 12. Lalu 12 / 3 menghasilkan 4.0 karena operator / menghasilkan float."),
        buat_soal("Jika p = 5 dan q = 2, hasil p ** q + p adalah ...", ["30", "25", "27", "35"], 0, "p ** q berarti 5 pangkat 2 = 25. Kemudian 25 + 5 = 30."),
        buat_soal("Apa keluaran dari x = 20; x = x % 6; print(x * 2)?", ["4", "8", "12", "14"], 0, "20 % 6 menghasilkan sisa 2. Kemudian 2 * 2 = 4. Jadi jawaban yang benar adalah 4.")
    ]
}


def buat_jendela_utama():
    jendela = tk.Tk()
    jendela.title(JUDUL_APLIKASI)
    jendela.geometry("700x500")
    jendela.configure(bg=WARNA_BACKGROUND)

    judul = tk.Label(
        jendela, text="MPI PEMROGRAMAN DASAR PYTHON",
        font=("Arial", 20, "bold"), bg=WARNA_BACKGROUND, fg=WARNA_UTAMA
    )
    judul.pack(pady=(40, 10))

    deskripsi = tk.Label(
        jendela, text="Media Pembelajaran Interaktif untuk Belajar Python",
        font=("Arial", 11), bg=WARNA_BACKGROUND
    )
    deskripsi.pack(pady=(0, 25))

    def tampilkan_materi(materi):
        halaman = tk.Toplevel(jendela)
        halaman.title(materi["judul"])
        halaman.geometry("650x550")
        halaman.configure(bg=WARNA_BACKGROUND)

        tk.Label(
            halaman, text=materi["judul"], font=("Arial", 18, "bold"),
            bg=WARNA_BACKGROUND, fg=WARNA_UTAMA
        ).pack(pady=20)

        tk.Label(
            halaman, text=materi["isi"], font=("Arial", 11),
            bg=WARNA_BACKGROUND, justify="left", wraplength=570
        ).pack(padx=30, pady=10, anchor="w")

        tk.Label(
            halaman, text="Contoh Kode Python:", font=("Arial", 12, "bold"),
            bg=WARNA_BACKGROUND, fg=WARNA_UTAMA
        ).pack(pady=(15, 5))

        kotak_kode = tk.Text(
            halaman, height=8, width=65, font=("Consolas", 11),
            bg="#e2e8f0", fg="#172554", relief="flat", padx=10, pady=10
        )
        kotak_kode.pack(padx=25, pady=5)
        kotak_kode.insert("1.0", materi["contoh"])
        kotak_kode.configure(state="disabled")

    def buka_materi():
        halaman_materi = tk.Toplevel(jendela)
        halaman_materi.title("Materi Pembelajaran")
        halaman_materi.geometry("600x450")
        halaman_materi.configure(bg=WARNA_BACKGROUND)

        tk.Label(
            halaman_materi, text="MATERI PEMBELAJARAN PYTHON",
            font=("Arial", 18, "bold"), bg=WARNA_BACKGROUND, fg=WARNA_UTAMA
        ).pack(pady=25)

        tk.Label(
            halaman_materi, text="Pilih materi yang ingin kamu pelajari:",
            font=("Arial", 11), bg=WARNA_BACKGROUND
        ).pack(pady=10)

        for materi in DATA_MATERI:
            tk.Button(
                halaman_materi, text=materi["judul"], font=("Arial", 12),
                bg="white", fg=WARNA_UTAMA, width=35, pady=10,
                command=lambda m=materi: tampilkan_materi(m)
            ).pack(pady=6)

    def buka_kuis():
        halaman_pilih = tk.Toplevel(jendela)
        halaman_pilih.title("Pilih Tingkat Kesulitan")
        halaman_pilih.geometry("500x400")
        halaman_pilih.configure(bg=WARNA_BACKGROUND)

        tk.Label(
            halaman_pilih, text="PILIH TINGKAT KESULITAN",
            font=("Arial", 18, "bold"), bg=WARNA_BACKGROUND, fg=WARNA_UTAMA
        ).pack(pady=(35, 15))

        tk.Label(
            halaman_pilih, text="Pilih tingkat kesulitan sebelum memulai kuis.",
            font=("Arial", 11), bg=WARNA_BACKGROUND
        ).pack(pady=8)

        tk.Label(
            halaman_pilih, text="Setiap kuis terdiri dari 10 soal pilihan ganda.",
            font=("Arial", 10), bg=WARNA_BACKGROUND
        ).pack(pady=5)

        def mulai_kuis(tingkat):
            halaman_pilih.destroy()
            jalankan_kuis(tingkat)

        for tingkat in ("Mudah", "Menengah", "Sulit"):
            tk.Button(
                halaman_pilih, text=tingkat.upper(),
                font=("Arial", 12, "bold"), bg=WARNA_UTAMA,
                fg="white", width=25, pady=10,
                command=lambda t=tingkat: mulai_kuis(t)
            ).pack(pady=8)

    def jalankan_kuis(tingkat, soal_terpilih=None):
        halaman_kuis = tk.Toplevel(jendela)
        halaman_kuis.title(f"Kuis Python - {tingkat}")
        halaman_kuis.geometry("700x620")
        halaman_kuis.configure(bg=WARNA_BACKGROUND)

        if soal_terpilih is None:
            soal_terpilih = random.sample(BANK_SOAL[tingkat], JUMLAH_SOAL_KUIS)

        nomor_soal = 0
        skor = 0
        jawaban_pilihan = tk.IntVar(value=-1)
        sudah_menjawab = False

        tk.Label(
            halaman_kuis, text=f"KUIS PYTHON - TINGKAT {tingkat.upper()}",
            font=("Arial", 17, "bold"), bg=WARNA_BACKGROUND, fg=WARNA_UTAMA
        ).pack(pady=18)

        label_nomor = tk.Label(
            halaman_kuis, text="", font=("Arial", 11, "bold"),
            bg=WARNA_BACKGROUND
        )
        label_nomor.pack(pady=5)

        label_soal = tk.Label(
            halaman_kuis, text="", font=("Arial", 13, "bold"),
            bg=WARNA_BACKGROUND, wraplength=620
        )
        label_soal.pack(pady=18)

        area_pilihan = tk.Frame(halaman_kuis, bg=WARNA_BACKGROUND)
        area_pilihan.pack(pady=8)

        area_pembahasan = tk.Frame(
            halaman_kuis, bg="#e2e8f0", padx=14, pady=10
        )
        label_status = tk.Label(
            area_pembahasan, text="", font=("Arial", 11, "bold"),
            bg="#e2e8f0", justify="left", wraplength=620
        )
        label_status.pack(anchor="w")

        label_pembahasan = tk.Label(
            area_pembahasan, text="", font=("Arial", 10),
            bg="#e2e8f0", justify="left", wraplength=620
        )
        label_pembahasan.pack(anchor="w", pady=(5, 0))

        tombol_lanjut = tk.Button(
            halaman_kuis, text="PERIKSA JAWABAN",
            font=("Arial", 11, "bold"), bg=WARNA_UTAMA,
            fg="white", width=24, pady=9
        )
        tombol_lanjut.pack(pady=16)

        def tampilkan_soal():
            nonlocal sudah_menjawab
            sudah_menjawab = False
            jawaban_pilihan.set(-1)
            data = soal_terpilih[nomor_soal]

            label_nomor.config(
                text=f"Soal {nomor_soal + 1} dari {JUMLAH_SOAL_KUIS}"
            )
            label_soal.config(text=data["soal"])

            for widget in area_pilihan.winfo_children():
                widget.destroy()

            for indeks, pilihan in enumerate(data["pilihan"]):
                tk.Radiobutton(
                    area_pilihan, text=f"{chr(65 + indeks)}. {pilihan}",
                    variable=jawaban_pilihan, value=indeks,
                    font=("Arial", 11), bg=WARNA_BACKGROUND,
                    anchor="w", width=65, padx=10, pady=6
                ).pack(anchor="w", pady=2)

            label_status.config(text="")
            label_pembahasan.config(text="")
            area_pembahasan.pack_forget()
            tombol_lanjut.config(text="PERIKSA JAWABAN")

        def lanjut_soal():
            nonlocal nomor_soal, skor, sudah_menjawab

            if not sudah_menjawab:
                pilihan = jawaban_pilihan.get()
                if pilihan == -1:
                    messagebox.showwarning(
                        "Peringatan",
                        "Silakan pilih salah satu jawaban terlebih dahulu.",
                        parent=halaman_kuis
                    )
                    return

                data = soal_terpilih[nomor_soal]
                jawaban_benar = data["jawaban"]
                teks_benar = data["pilihan"][jawaban_benar]

                if pilihan == jawaban_benar:
                    skor += 1
                    label_status.config(
                        text="BENAR! Jawaban kamu tepat.",
                        fg="#166534"
                    )
                else:
                    label_status.config(
                        text=f"BELUM TEPAT. Jawaban yang benar: "
                             f"{chr(65 + jawaban_benar)}. {teks_benar}",
                        fg="#991b1b"
                    )

                pembahasan = data.get("pembahasan") or (
                    f"Jawaban yang benar adalah {teks_benar}. "
                    "Pelajari kembali materi terkait agar semakin memahami "
                    "konsep yang ditanyakan."
                )
                label_pembahasan.config(text=pembahasan)
                area_pembahasan.pack(
                    fill="x", padx=22, pady=10
                )
                sudah_menjawab = True
                tombol_lanjut.config(
                    text="LIHAT HASIL" if nomor_soal == JUMLAH_SOAL_KUIS - 1
                    else "SOAL BERIKUTNYA"
                )
                return

            if nomor_soal < JUMLAH_SOAL_KUIS - 1:
                nomor_soal += 1
                tampilkan_soal()
            else:
                tampilkan_hasil()

        def tampilkan_hasil():
            for widget in halaman_kuis.winfo_children():
                widget.destroy()

            nilai = int((skor / JUMLAH_SOAL_KUIS) * 100)

            tk.Label(
                halaman_kuis, text="HASIL KUIS",
                font=("Arial", 22, "bold"), bg=WARNA_BACKGROUND,
                fg=WARNA_UTAMA
            ).pack(pady=(30, 15))

            tk.Label(
                halaman_kuis, text=f"Tingkat Kesulitan: {tingkat}",
                font=("Arial", 12), bg=WARNA_BACKGROUND
            ).pack(pady=5)

            tk.Label(
                halaman_kuis,
                text=f"Jawaban benar: {skor} dari {JUMLAH_SOAL_KUIS} soal",
                font=("Arial", 14), bg=WARNA_BACKGROUND
            ).pack(pady=8)

            tk.Label(
                halaman_kuis, text=f"Nilai Akhir: {nilai}",
                font=("Arial", 20, "bold"), bg=WARNA_BACKGROUND,
                fg=WARNA_UTAMA
            ).pack(pady=10)

            pesan = (
                "Bagus! Kamu sudah memahami materi Python."
                if nilai >= 70
                else "Tetap semangat! Pelajari kembali materi Python."
            )
            tk.Label(
                halaman_kuis, text=pesan, font=("Arial", 11),
                bg=WARNA_BACKGROUND, wraplength=550
            ).pack(pady=8)

            tk.Label(
                halaman_kuis,
                text="Apa yang ingin kamu lakukan selanjutnya?",
                font=("Arial", 11, "bold"), bg=WARNA_BACKGROUND
            ).pack(pady=(15, 8))

            def ulangi_soal_sama():
                halaman_kuis.destroy()
                jalankan_kuis(tingkat, soal_terpilih)

            def coba_soal_berbeda():
                halaman_kuis.destroy()
                soal_lama = {item["soal"] for item in soal_terpilih}
                soal_tersedia = [
                    item for item in BANK_SOAL[tingkat]
                    if item["soal"] not in soal_lama
                ]

                if len(soal_tersedia) < JUMLAH_SOAL_KUIS:
                    messagebox.showinfo(
                        "Informasi",
                        "Tidak tersedia cukup soal baru. Kuis akan "
                        "menggunakan kembali bank soal dengan kombinasi acak.",
                        parent=jendela
                    )
                    soal_baru = random.sample(
                        BANK_SOAL[tingkat], JUMLAH_SOAL_KUIS
                    )
                else:
                    soal_baru = random.sample(
                        soal_tersedia, JUMLAH_SOAL_KUIS
                    )

                jalankan_kuis(tingkat, soal_baru)

            tk.Button(
                halaman_kuis, text="ULANGI SOAL YANG SAMA",
                font=("Arial", 10, "bold"), bg=WARNA_UTAMA,
                fg="white", width=27, pady=8,
                command=ulangi_soal_sama
            ).pack(pady=5)

            tk.Button(
                halaman_kuis, text="COBA SOAL BERBEDA",
                font=("Arial", 10, "bold"), bg="#315f8c",
                fg="white", width=27, pady=8,
                command=coba_soal_berbeda
            ).pack(pady=5)

            tk.Button(
                halaman_kuis, text="KEMBALI KE MENU UTAMA",
                font=("Arial", 10, "bold"), bg="white",
                fg=WARNA_UTAMA, width=27, pady=8,
                command=halaman_kuis.destroy
            ).pack(pady=5)

        tombol_lanjut.config(command=lanjut_soal)
        tampilkan_soal()

    def buka_tentang():
        messagebox.showinfo(
            "Tentang Aplikasi",
            "MPI Pemrograman Dasar Python adalah aplikasi "
            "pembelajaran interaktif untuk mempelajari dasar Python."
        )

    def keluar_aplikasi():
        konfirmasi = messagebox.askyesno(
            "Keluar", "Apakah kamu yakin ingin keluar dari aplikasi?"
        )
        if konfirmasi:
            jendela.destroy()

    daftar_menu = [
        ("MATERI PEMBELAJARAN", buka_materi),
        ("KUIS", buka_kuis),
        ("TENTANG APLIKASI", buka_tentang),
        ("KELUAR", keluar_aplikasi)
    ]

    for teks, fungsi in daftar_menu:
        tk.Button(
            jendela, text=teks, font=("Arial", 11, "bold"),
            bg=WARNA_UTAMA, fg="white", width=28, pady=9,
            command=fungsi
        ).pack(pady=6)

    return jendela


if __name__ == "__main__":
    aplikasi = buat_jendela_utama()
    aplikasi.mainloop()
