"""
MODUL 1: PENGENALAN TKINTER & WIDGET DASAR
==========================================

Apa itu Tkinter?
Tkinter adalah pustaka standar Python untuk membuat antarmuka pengguna grafis (GUI).
Ini adalah 'binding' ke toolkit GUI Tk.

Struktur Dasar Aplikasi Tkinter:
1. Import module: `import tkinter as tk`
2. Buat instance jendela utama: `root = tk.Tk()`
3. Tambahkan widget (Label, Button, dll) ke dalam jendela.
4. Jalankan loop acara utama: `root.mainloop()`

Widget yang akan dipelajari di bagian ini:
1. Window (Jendela Utama)
2. Label (Teks statis)
3. Button (Tombol interaktif)
4. Entry (Input teks satu baris)
"""

import tkinter as tk
from tkinter import font

def main():
    # --- 1. MEMBUAT JENDELA UTAMA ---
    root = tk.Tk()
    
    # Mengatur judul jendela
    root.title("Belajar Tkinter - Bagian 1")
    
    # Mengatur ukuran awal (Lebar x Tinggi + Posisi X + Posisi Y)
    root.geometry("400x500")
    
    # Mengatur apakah jendela bisa diubah ukurannya (Resizable)
    # (Horizontal/Width, Vertical/Height) -> (False, False) berarti tetap.
    root.resizable(True, True) 
    
    # Mengatur warna latar belakang jendela
    root.configure(bg="#f0f0f0") 

    # --- 2. WIDGET LABEL ---
    # Label digunakan untuk menampilkan teks atau gambar.
    # Parameter umum: text, font, bg (background), fg (foreground/text color), 
    # width, height, anchor, justify.
    
    # Membuat font custom
    custom_font = font.Font(family="Helvetica", size=12, weight="bold")
    
    label_judul = tk.Label(
        root, 
        text="Selamat Datang di Tkinter!",
        font=("Arial", 16, "bold"), # Font, size, style
        fg="white",                 # Warna teks
        bg="#3498db",               # Warna background label
        pady=10,                    # Padding vertikal internal
        width=30                    # Lebar dalam satuan karakter (approx)
    )
    # pack() adalah layout manager sederhana (akan dibahas detail di Part 2)
    label_judul.pack(pady=10) # pady di pack adalah margin vertikal eksternal

    label_info = tk.Label(root, text="Ini adalah contoh penggunaan Label.\nLabel bisa multi-line.", justify="center")
    label_info.pack()

    # --- 3. WIDGET ENTRY ---
    # Entry digunakan untuk menerima input teks satu baris dari user.
    
    label_input = tk.Label(root, text="Masukkan Nama Anda:")
    label_input.pack(pady=(20, 5)) # margin top 20, bottom 5
    
    entry_nama = tk.Entry(
        root, 
        width=30, 
        font=("Arial", 10),
        bd=2,       # Border width
        relief="sunken" # Gaya border: flat, sunke, raised, groove, ridge
    )
    entry_nama.pack()
    
    # Tips: Untuk input password, gunakan parameter show="*"
    # entry_pass = tk.Entry(root, show="*")

    # --- 4. WIDGET BUTTON ---
    # Button digunakan untuk memicu aksi.
    
    # Fungsi yang akan dipanggil saat tombol ditekan
    def sapa_user():
        nama = entry_nama.get() # Mengambil teks dari Entry
        if nama:
            label_hasil.config(text=f"Halo, {nama}! Semangat belajar!", fg="green")
        else:
            label_hasil.config(text="Mohon masukkan nama terlebih dahulu!", fg="red")
            
    def hapus_input():
        entry_nama.delete(0, tk.END) # Menghapus teks dari indeks 0 sampai akhir
        label_hasil.config(text="Siap menyapa...", fg="black")

    # Frame untuk menampung tombol agar rapi (Opsional, preview untuk materi Container)
    frame_tombol = tk.Frame(root, bg="#f0f0f0")
    frame_tombol.pack(pady=20)

    btn_sapa = tk.Button(
        frame_tombol, 
        text="Sapa Saya",
        command=sapa_user,       # Fungsi dipanggil TANPA kurung ()
        bg="#2ecc71",            # Warna tombol
        fg="white",
        activebackground="#27ae60", # Warna saat ditekan
        activeforeground="white",
        width=10
    )
    btn_sapa.pack(side=tk.LEFT, padx=5)

    btn_hapus = tk.Button(
        frame_tombol, 
        text="Hapus", 
        command=hapus_input,
        bg="#e74c3c",
        fg="white",
        width=10
    )
    btn_hapus.pack(side=tk.LEFT, padx=5)

    # Label untuk menampilkan hasil interaksi
    label_hasil = tk.Label(root, text="Siap menyapa...", font=("Arial", 10, "italic"), bg="#f0f0f0")
    label_hasil.pack(pady=10)

    # Menjalankan aplikasi
    root.mainloop()

if __name__ == "__main__":
    main()

"""
===========================================================================
LATIHAN SOAL - BAGIAN 1 (INTRO & WIDGET DASAR)
===========================================================================

Kerjakan soal-soal di bawah ini dalam file terpisah untuk melatih pemahamanmu.

--- MUDAH (5 Soal) ---
1. Buatlah sebuah jendela Tkinter sederhana dengan judul "Aplikasi Pertamaku" dan ukuran 300x200 pixel.
2. Tambahkan sebuah Label di tengah jendela bertuliskan "Saya Sedang Belajar Python Tkinter" dengan warna teks biru.
3. Buatlah sebuah tombol (Button) dengan tulisan "Klik Saya". Ketika diklik, tombol tersebut mencetak string "Tombol diklik!" ke terminal (console).
4. Buatlah sebuah Entry widget. Di bawahnya, buat tombol "Ambil Teks". Jika tombol diklik, cetak isi teks Entry ke terminal.
5. Cobalah ubah warna background jendela utama menjadi warna favoritmu (gunakan kode hex, misal "#FFFF00" untuk kuning).

--- MENENGAH (5 Soal) ---
6. Buat aplikasi "Penghitung Karakter". Ada satu Entry dan satu Label. Setiap kali user mengetik dan menekan tombol "Hitung", Label menampilkan jumlah karakter yang diketik.
7. Buat aplikasi sederhana dengan dua tombol: "Besar" dan "Kecil". Ada satu Label "CONTOH TEKS". Jika tombol "Besar" ditekan, font label menjadi besar (size 20). Jika "Kecil" ditekan, kembali ke size 10.
8. Buat form login sederhana (tampilan saja). Ada Label "Username", Entry Username, Label "Password", Entry Password (huruf harus jadi bintang '*'), dan tombol "Login".
9. Buat aplikasi counter sederhana. Ada Label angka "0" dan tombol "Tambah". Setiap tombol ditekan, angka di Label bertambah 1.
10. Eksperimen dengan properti `state` pada Button. Buat Entry dan Tombol "Submit". Tombol "Submit" terkunci (disabled) secara default. Tambahkan tombol lain "Aktifkan" yang jika diklik akan mengaktifkan tombol "Submit".

--- SULIT (5 Soal) ---
11. Buat aplikasi "Kalkulator Mini" yang hanya bisa penjumlahan. Ada 2 Entry untuk angka pertama dan kedua. Ada tombol "+". Di bawahnya ada Label hasil. Tampilkan pesan error di Label jika user memasukkan bukan angka (gunakan try-except saat mengambil data).
12. Buat widget "Lampu Lalu Lintas". Ada 3 Label bulat (atau kotak) yang ditumpuk vertikal (Merah, Kuning, Hijau - awalnya abu-abu semua). Ada tombol "Ganti" yang jika ditekan akan menyalakan lampu secara bergantian (Merah -> Kuning -> Hijau -> Merah dst). *Hint: Ubah properti 'bg' secara bergantian*.
13. Buat program yang memiliki satu Label angka acak (1-100) dan satu Tombol "Acak Lagi". Gunakan modul `random`. Setiap diklik, angka berubah.
14. Buat aplikasi "Color Picker" manual. Ada 3 Entry (R, G, B). User memasukkan angka 0-255. Saat tombol "Preview" ditekan, background jendela berubah sesuai warna RGB tersebut. *Hint: Konversi angka ke Hex String (misal #FF00AA)*.
15. (Tantangan Logika) Buat satu tombol yang posisinya pindah-pindah secara acak di dalam window setiap kali cursor mouse mendekatinya (hover) atau setiap kali diklik, sehingga sulit diklik. *Hint: Gunakan method .place(x=..., y=...) dan random*. Sebenarnya layout manager belum dibahas detail, tapi coba cari tahu basic penggunaannya.
"""
