"""
MODUL 2: LAYOUT MANAGEMENT (PENGATURAN TATA LETAK)
==================================================

Dalam Tkinter, widget tidak akan muncul kecuali jika Anda menempatkannya menggunakan 'Geometry Manager'.
Ada 3 metode (manager) utama:
1. .pack()  -> Menumpuk widget secara vertikal atau horizontal. Sederhana tapi terbatas.
2. .grid()  -> Menempatkan widget dalam struktur baris dan kolom (seperti Excel/Tabel). Paling sering digunakan.
3. .place() -> Menempatkan widget pada koordinat piksel absolut atau relatif. Presisi tapi sulit dikelola jika ukuran window berubah.

ATURAN EMAS: Jangan gunakan .pack() dan .grid() bersamaan di dalam SATU container/window induk yang sama. Error akan terjadi.

"""

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Belajar Layout - Bagian 2")
    root.geometry("600x600")

    # --- 1. PACK() ---
    # Konsep: "Side" (arah tumpukan), "Fill" (isi ruang), "Expand" (ambil sisa ruang).
    
    label_pack = tk.Label(root, text="--- CONTOH PACK ---", bg="yellow", width=100)
    label_pack.pack() # Default: side=TOP
    
    # Frame untuk demo pack agar terpisah dari grid di bawahnya (biasanya dipisah frame)
    frame_pack = tk.Frame(root, bd=2, relief="groove")
    frame_pack.pack(pady=10, fill=tk.X, padx=10)

    btn1 = tk.Button(frame_pack, text="LEFT", bg="red", fg="white")
    btn1.pack(side=tk.LEFT, padx=5, pady=5)

    btn2 = tk.Button(frame_pack, text="RIGHT", bg="blue", fg="white")
    btn2.pack(side=tk.RIGHT, padx=5, pady=5)

    btn3 = tk.Button(frame_pack, text="TOP (Fill X)", bg="green", fg="white")
    btn3.pack(side=tk.TOP, fill=tk.X, padx=5) # Mengisi lebar horizontal yang tersedia

    btn4 = tk.Button(frame_pack, text="BOTTOM", bg="orange")
    btn4.pack(side=tk.BOTTOM, padx=5)


    # --- 2. GRID() ---
    # Konsep: Row (Baris, 0-N), Column (Kolom, 0-N).
    # Sticky: Menempel ke arah mana dalam sel (N, S, W, E - arah mata angin). N=Atas, S=Bawah, W=Kiri, E=Kanan.
    
    label_grid = tk.Label(root, text="--- CONTOH GRID ---", bg="cyan", width=100)
    label_pack.pack() 
    # Karena root sudah pakai pack utk label_pack, kita HARUS buat Frame BARU untuk area Grid
    # agar tidak campur pack & grid langsung di root yang sama.
    
    container_grid = tk.Frame(root, bd=2, relief="solid")
    container_grid.pack(pady=20) # Container ini di-pack ke root, di dalamnya kita pakai grid

    # Baris 0
    tk.Label(container_grid, text="Nama Depan").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    tk.Entry(container_grid).grid(row=0, column=1, padx=5, pady=5)

    # Baris 1
    tk.Label(container_grid, text="Nama Belakang").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    tk.Entry(container_grid).grid(row=1, column=1, padx=5, pady=5)

    # Baris 2 (Tombol yang lebar melintasi 2 kolom)
    tk.Button(container_grid, text="Submit (Columnspan=2)", bg="lightgrey").grid(row=2, column=0, columnspan=2, sticky="we", padx=5, pady=5)


    # --- 3. PLACE() ---
    # Konsep: x, y (piksel). Atau relx, rely (0.0 - 1.0 persentase posisi).
    
    container_place = tk.Frame(root, width=300, height=150, bg="lightpink")
    container_place.pack(pady=20)
    # Penting: Container untuk place harus punya ukuran fixed atau diatur proporsinya,
    # karena widget di dalamnya tidak mendorong ukuran container.
    
    tk.Label(container_place, text="Mode Place (Absolute)", bg="white").place(x=10, y=10)
    tk.Label(container_place, text="x=50, y=50", bg="white").place(x=50, y=50)
    
    # Relative placement (Tengah-tengah container)
    tk.Button(container_place, text="Center (relx=0.5, rely=0.5)").place(relx=0.5, rely=0.5, anchor="center")

    root.mainloop()

if __name__ == "__main__":
    main()

"""
===========================================================================
LATIHAN SOAL - BAGIAN 2 (LAYOUT MANAGEMENT)
===========================================================================

Gunakan Frame jika perlu untuk memisahkan area latihan di satu window, atau buat file terpisah.

--- MUDAH (5 Soal) ---
1. Buat 3 tombol ("Merah", "Kuning", "Hijau"). Gunakan `.pack()` untuk menyusunnya berjajar HORIZONTAL (kiri ke kanan).
2. Buat 3 tombol ("Atas", "Tengah", "Bawah"). Gunakan `.pack()` vertikal. Tombol "Tengah" harus mengisi lebar layar (`fill=tk.X`).
3. Buat Layout Grid 2x2 sederhana. 
   - (0,0) Label "A"
   - (0,1) Label "B"
   - (1,0) Label "C"
   - (1,1) Label "D"
4. Tempatkan sebuah tombol tepat di pojok kanan bawah window ukuran 300x300 menggunakan `.place()` (hitunga koordinat matematika sederhana atau relx/rely).
5. Buat sebuah Label yang menempel di `side=tk.BOTTOM` dengan background hitam dan text putih, mirip seperti "Status Bar".

--- MENENGAH (5 Soal) ---
6. Desain Form Registrasi sederhana menggunakan `.grid()`. 
   Field: Nama Lengkap, Email, Password, Konfirmasi Password. Label rata kiri (`sticky='w'`), Entry rata kiri. Tombol Register di bawah, rata tengah lebar penuh.
7. Buat tampilan seperti keypad HP/Kalkulator (Angka 1-9) dalam grid 3x3.
8. Gunakan `.pack()`: Buat layout dengan sidebar di kiri (lebar tetap), header di atas, dan area konten utama di sisa ruang (`side=LEFT`, `side=TOP`...).
9. Gunakan `.grid()` dengan `rowspan`. Buat sebuah gambar (atau Label besar berwarna) di kolom 0 yang tingginya memakan 3 baris. Di kolom 1, ada 3 Label kecil berurutan baris 0, 1, 2.
10. Eksplorasi `padding`: Buat grid 2x2 Button. Berikan `padx` dan `pady` eksternal yang besar antar tombol, dan `ipadx` `ipady` (internal padding) agar tombol terlihat gemuk.

--- SULIT (5 Soal) ---
11. **Tantangan Chessboard**: Buat papan catur 8x8 menggunakan `.grid()`. Gunakan loop (for i in range(8)) daripada menulis manual. Warnai selang-seling hitam dan putih menggunakan Label dengan width/height tertentu.
12. **Layout Responsif**: Buat 4 tombol dalam grid 2x2. Gunakan `rowconfigure` dan `columnconfigure` pada parent window dengan `weight=1`. Coba resize window, pastikan tombol ikut membesar/mengecil secara proporsional.
13. **Center Window**: Buat fungsi agar saat aplikasi dijalankan, window langsung muncul tepat di TENGAH layar monitor user, berapapun resolusinya. *Hint: Ambil screen width/height via `root.winfo_screenwidth()` lalu hitung koordinat geometry*.
14. Buat layout Dashboard Admin mockup: 
   - Header (Top)
   - Sidebar Menu (Left) berisi 5 tombol.
   - Main Content (Right/Center) berisi grid statistik sederhana.
   - Footer (Bottom).
   Gunakan kombinasi Frame dan pack/grid yang tepat.
15. **Place Animation**: Buat sebuah Label "Bola" (teks "O"). Buat tombol "Gerak". Saat tombol ditekan, looping koordinat `place` untuk menggerakkan label dari kiri ke kanan secara perlahan (animasi sederhana). *Hint: Butuh `root.after()` atau `time.sleep` (hati-hati blocking) untuk animasi*.
"""
