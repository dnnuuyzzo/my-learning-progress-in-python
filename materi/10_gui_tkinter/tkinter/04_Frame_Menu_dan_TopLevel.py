"""
MODUL 4: PENGORGANISASIAN GUI & WINDOW BARU (FRAME, MENU, TOPLEVEL)
===================================================================

Semakin kompleks aplikasi, kita tidak bisa hanya menumpuk widget di `root`.
Kita butuh wadah (Container) dan window tambahan.

A. FRAME & LABELFRAME
---------------------
- `Frame`: Widget kontainer kotak kosong. Digunakan untuk mengelompokkan widget lain agar layout lebih rapi.
- `LabelFrame`: Mirip Frame, tapi memiliki garis batas (border) dan label judul. Bagus untuk grouping setting form.

B. MENU BAR
-----------
Menu standar di bagian atas aplikasi (File, Edit, Help, dll).
Struktur: Menu Bar (induk) -> Menu (anak) -> Command (item).

C. TOPLEVEL (WINDOW TAMBAHAN)
-----------------------------
Membuat jendela baru terpisah dari jendela utama (`root`). 
Biasanya untuk jendela settings, pop-up custom, atau detail info.
PENTING: Jangan buat instance `tk.Tk()` lagi. Gunakan `tk.Toplevel()` untuk window kedua dst.

"""

import tkinter as tk
from tkinter import messagebox # Kita import messagebox untuk demo menu

def main():
    root = tk.Tk()
    root.title("Organisasi GUI & Menu - Bagian 4")
    root.geometry("600x400")

    # --- 1. MENUBAR ---
    # Langkah 1: Buat Menu Bar utama
    menubar = tk.Menu(root)
    
    # Langkah 2: Buat Menu "File"
    file_menu = tk.Menu(menubar, tearoff=0) # tearoff=0 agar menu tidak bisa "disobek/dilepas"
    file_menu.add_command(label="New Project", command=lambda: print("New Project Clicked"))
    file_menu.add_command(label="Open", command=lambda: print("Open Clicked"))
    file_menu.add_separator() # Garis pemisah
    file_menu.add_command(label="Exit", command=root.quit)
    
    # Langkah 3: Tempel Menu "File" ke Menu Bar Utama
    menubar.add_cascade(label="File", menu=file_menu)

    # Menu "Help"
    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Aplikasi Belajar Tkinter v1.0"))
    menubar.add_cascade(label="Help", menu=help_menu)

    # Langkah 4: Config root untuk menggunakan menubar ini
    root.config(menu=menubar)


    # --- 2. FRAME & LABELFRAME (Layouting) ---
    
    # Sisi Kiri: Panel Navigasi (Frame biasa)
    left_frame = tk.Frame(root, bg="#34495e", width=150)
    left_frame.pack(side=tk.LEFT, fill=tk.Y)
    # Agar frame tetap punya width meski widget child kecil, gunakan pack_propagate(False) jika perlu,
    # tapi biasanya kita biarkan frame menyesuaikan isi.
    
    tk.Label(left_frame, text="SIDEBAR", bg="#34495e", fg="white", font=("Arial", 12, "bold")).pack(pady=20)
    tk.Button(left_frame, text="Dashboard", width=15).pack(pady=5)
    tk.Button(left_frame, text="Settings", width=15).pack(pady=5)

    # Sisi Kanan: Konten Utama
    main_frame = tk.Frame(root, bg="white") # Frame tak terlihat, hanya grouping
    main_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

    tk.Label(main_frame, text="Halaman Utama", font=("Arial", 18), bg="white").pack(pady=20)

    # LabelFrame untuk Grouping Form
    group_frame = tk.LabelFrame(main_frame, text="User Data", padx=10, pady=10, bg="white")
    group_frame.pack(padx=20, pady=10, fill=tk.X)

    tk.Label(group_frame, text="Nama:", bg="white").grid(row=0, column=0, sticky="w")
    tk.Entry(group_frame).grid(row=0, column=1)
    
    tk.Label(group_frame, text="Email:", bg="white").grid(row=1, column=0, sticky="w")
    tk.Entry(group_frame).grid(row=1, column=1)


    # --- 3. TOPLEVEL (Jendela Baru) ---
    def buka_jendela_baru():
        top = tk.Toplevel(root) # Window anak dari root
        top.title("Settings Window")
        top.geometry("300x200")
        
        # Jendela ini independen tapi akan tertutup jika root ditutup
        tk.Label(top, text="Ini adalah Jendela Kedua (TopLevel)").pack(pady=20)
        tk.Button(top, text="Tutup", command=top.destroy).pack()
        
        # Opsional: Bikin jendela ini "Modal" (fokus terkunci di sini sampai ditutup)
        # top.transient(root) 
        # top.grab_set() 
        # root.wait_window(top)

    tk.Button(main_frame, text="Buka Jendela Baru", command=buka_jendela_baru, bg="orange").pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()

"""
===========================================================================
LATIHAN SOAL - BAGIAN 4 (FRAME, MENU, TOPLEVEL)
===========================================================================

--- MUDAH (5 Soal) ---
1. Buat aplikasi dengan Menubar standar. Tambahkan menu "File" dengan item "Exit" yang menutup aplikasi.
2. Buat layout window yang dibagi dua secara vertikal menggunakan Frame. Frame kiri background merah, Frame kanan background biru. Masing-masing mengisi separuh layar.
3. Buat LabelFrame bertuliskan "Alamat Pengiriman". Di dalamnya ada Entry untuk "Jalan", "Kota", dan "Kode Pos".
4. Buat tombol "Info Lain". Jika diklik, memunculkan jendela baru (`Toplevel`) berukuran kecil 200x100 dengan pesan text "Hello World".
5. Di dalam jendela `Toplevel` pada soal no 4, tambahkan tombol "Close" yang berfungsi menutup jendela tersebut (`.destroy()`).

--- MENENGAH (5 Soal) ---
6. **Nested Frames**: Buat Frame 'Parent' dengan border tebal. Di dalamnya, buat 2 Frame 'Child' (Atas dan Bawah). Di Frame Atas taruh Label, di Frame Bawah taruh Tombol.
7. **Menu Checkbutton**: Di menu "View", tambahkan item Checkbutton "Show Toolbar". Gunakan variable boolean. Saat dicentang/uncentang, print statusnya ke console.
8. **Login Popup**: Window utama hanya berisi tombol "Login". Saat diklik, muncul Toplevel berisi Form Login (User/Pass). Jika login "Benar" (hardcode), Toplevel tertutup dan text tombol window utama berubah jadi "Welcome, Admin".
9. **Modal Dialog Manual**: Buat Toplevel yang memaksa user menutupnya sebelum bisa klik window utama lagi (Lihat hint `grab_set()` di materi).
10. **Tab Layout (Manual)**: Buat frame navigasi atas berisi Tombol "Tab 1", "Tab 2". Di bawahnya ada Frame Konten. Jika tombol "Tab 1" diklik, Frame Konten dibersihkan lalu diisi konten 1. Jika "Tab 2", diisi konten 2. (Simulasi Tab sederhana tanpa widget Notebook).

--- SULIT (5 Soal) ---
11. **Text Editor Layout Clone**: Buat layout statis mirip Notepad/VS Code sederhana. 
    - Menubar di atas.
    - Sidebar kiri tipis (Frame).
    - Status bar di bawah (Label dlm Frame).
    - Area tengah kosong (putih) yang luas.
12. **Aplikasi Multi-Window**: Window Utama = Daftar Barang (List). Ada tombol "Tambah Barang" -> Muncul Toplevel Form Input. Saat di-Submit di Toplevel, data dikirim kembali ke Window Utama (Print dulu aja datanya). *Hint: Passing function dari parent ke child window*.
13. **Right-Click Context Menu**: Buat Text area (atau Frame kosong). Jika diklik kanan, muncul Menu Popup kecil ("Cut", "Copy", "Paste") tepat di posisi mouse.
14. **Custom Title Bar**: (Advance) Buat window dengan `root.overrideredirect(True)` (menghilangkan border system OS). Lalu buat Frame sendiri di bagian atas window sebagai pengganti Title Bar (ada tombol X merah custom untuk keluar). Hati-hati aplikasi tidak bisa digeser (drag), perlu binding event motion untuk drag window manual.
15. **Responsive Grid Dashboard**: Buat 4 LabelFrame "Card" Statistik.
    - Pada ukuran window kecil, susunan 1 kolom (vertikal).
    - Pada ukuran window besar (maximize), sususnan otomatis jadi 2 baris x 2 kolom atau 1 baris x 4 kolom.
    *Hint: Gunakan event `<Configure>` pada root untuk mendeteksi perubahan ukuran window dan atur ulang layout `.grid()`*.
"""
