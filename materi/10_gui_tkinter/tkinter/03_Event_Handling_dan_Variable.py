"""
MODUL 3: EVENT HANDLING & CONTROL VARIABLES
===========================================

Interaksi adalah kunci GUI. Di modul ini kita belajar bagaimana merespons aksi user (klik, ketik, mouse move)
dan mengelola data widget menggunakan Variabel Khusus Tkinter.

A. EVENT HANDLING
-----------------
1. `command=func`: Cara termudah, biasanya ada di Button.
2. `.bind('<Event>', func)`: Cara advanced. Bisa untuk widget apa saja (termasuk Label, Frame, Entry).
   Format Event umum:
   - <Button-1> : Klik Kiri Mouse
   - <Button-3> : Klik Kanan Mouse
   - <Return>   : Tombol Enter pada keyboard
   - <Key>      : Tombol keyboard apapun
   - <Motion>   : Pergerakan mouse

B. CONTROL VARIABLES
--------------------
Variabel Python biasa (misal `x = 10`) tidak otomatis mengupdate UI jika nilainya berubah.
Tkinter punya tipe data khusus/wrapper yang "sadar" perubahan:
- `tk.StringVar()`
- `tk.IntVar()`
- `tk.BooleanVar()`
- `tk.DoubleVar()`

Keuntungan: Jika variable ini diubah `.set()`, widget yang terikat otomatis berubah tampilannya. Sebaliknya, jika widget diubah user, variabel ikut berubah.

C. WIDGET PILIHAN
-----------------
- `Checkbutton` (Checkbox): Butuh Variable boolean/int.
- `Radiobutton` (Opsi eksklusif): Butuh Variable yang SAMA untuk satu grup radiobutton.

"""

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Event Handling & Variables")
    root.geometry("500x500")

    # --- 1. EVENT BINDING ---
    lbl_info = tk.Label(root, text="Klik Saya (Kiri/Kanan) atau Tekan Enter", bg="lightgray", pady=10)
    lbl_info.pack(pady=10, fill=tk.X)

    # Handler function wajib menerima parameter 'event' jika dipanggil via bind
    def on_left_click(event):
        lbl_info.config(text=f"Klik Kiri di posisi: {event.x}, {event.y}")
        
    def on_right_click(event):
        lbl_info.config(text="Klik Kanan Terdeteksi!")
        
    def on_enter_key(event):
        lbl_info.config(text="Tombol ENTER ditekan!")

    # Binding
    lbl_info.bind("<Button-1>", on_left_click) # Klik Kiri
    lbl_info.bind("<Button-3>", on_right_click) # Klik Kanan
    root.bind("<Return>", on_enter_key) # Bind Enter ke window utama (global context)


    # --- 2. CONTROL VARIABLES & CHECKBUTTON ---
    frame_var = tk.LabelFrame(root, text="Control Variables", padx=10, pady=10)
    frame_var.pack(pady=20, fill=tk.X, padx=10)

    # StringVar example
    nama_var = tk.StringVar(value="User") # Default value
    
    entry_nama = tk.Entry(frame_var, textvariable=nama_var) 
    entry_nama.pack()
    
    lbl_sapa = tk.Label(frame_var, text="Halo...")
    lbl_sapa.pack()
    
    # Fungsi callback saat tombol ditekan
    def update_label():
        # Mengambil value dari variable
        nama = nama_var.get() 
        lbl_sapa.config(text=f"Halo, {nama} (Dynamic)!")
        
    btn_update = tk.Button(frame_var, text="Update Label via Get", command=update_label)
    btn_update.pack(pady=5)

    # Hint: Variable var_nama di atas terikat dengan Entry. 
    # Apapun yg diketik user otomatis masuk ke var_nama.


    # Checkbutton
    status_var = tk.BooleanVar() # Default False
    
    def on_check():
        if status_var.get():
            lbl_check_status.config(text="Status: ON", fg="green")
        else:
            lbl_check_status.config(text="Status: OFF", fg="red")

    chk = tk.Checkbutton(frame_var, text="Aktifkan Mode", var=status_var, command=on_check)
    chk.pack(pady=5)
    
    lbl_check_status = tk.Label(frame_var, text="Status: OFF", fg="red")
    lbl_check_status.pack()


    # --- 3. RADIOBUTTON ---
    frame_radio = tk.LabelFrame(root, text="Pilih Warna", padx=10, pady=10)
    frame_radio.pack(pady=10, fill=tk.X, padx=10)

    warna_var = tk.StringVar(value="white") # Default

    def ganti_bg():
        pilihan = warna_var.get()
        root.configure(bg=pilihan)

    # Perhatikan: variable=warna_var SAMA untuk semua opsi
    rb1 = tk.Radiobutton(frame_radio, text="Merah", variable=warna_var, value="#ffcccc", command=ganti_bg)
    rb2 = tk.Radiobutton(frame_radio, text="Hijau", variable=warna_var, value="#ccffcc", command=ganti_bg)
    rb3 = tk.Radiobutton(frame_radio, text="Biru", variable=warna_var, value="#ccccff", command=ganti_bg)
    
    rb1.pack(anchor="w")
    rb2.pack(anchor="w")
    rb3.pack(anchor="w")

    root.mainloop()

if __name__ == "__main__":
    main()

"""
===========================================================================
LATIHAN SOAL - BAGIAN 3 (EVENT & VARIABLES)
===========================================================================

--- MUDAH (5 Soal) ---
1. Buat sebuah Label "0". Binding event `<Button-1>` pada label tersebut agar setiap diklik angkanya bertambah 1.
2. Buat sebuah Entry dan Label. Gunakan `StringVar` pada Entry. Buat tombol yang jika diklik akan mengubah isi Entry menjadi text "Reset Berhasil" menggunakan method `.set()`.
3. Buat 2 Radiobutton: "Laki-laki" dan "Perempuan". Tambahkan tombol "Submit". Saat submit diklik, print pilihan user ke console.
4. Buat Checkbutton "Setuju Syarat & Ketentuan". Buat tombol "Lanjut" yang state-nya DISABLED (mati). Jika checkbutton dicentang, tombol "Lanjut" menjadi NORMAL (aktif). Gunakan `command=` pada checkbutton.
5. Binding tombol Keyboard: Buat label kosong. Jika user menekan tombol 'a' pd keyboard, label muncul tulisan "Huruf A ditekan".

--- MENENGAH (5 Soal) ---
6. **Live Typing Mirror**: Buat Entry dan Label. Tanpa tombol, setiap karakter yang diketik di Entry langsung muncul juga di Label secara realtime (gunakan `trace()` pada StringVar atau binding `<KeyRelease>`).
7. **Mouse Tracker**: Widget Label yang selalu menampilkan koordinat mouse (X, Y) saat mouse bergerak di atas window utama (`<Motion>`).
8. **Simple Quiz**: Buat pertanyaan "Berapa 5 + 5?". Berikan 3 Radiobutton pilihan jawaban (9, 10, 11). Jika user memilih 10, muncul label "Benar!". Jika salah, "Salah!".
9. **Focus Event**: Buat Entry. Jika cursor masuk ke Entry (`<FocusIn>`), ubah background Entry jadi kuning muda. Jika keluar (`<FocusOut>`), kembali putih.
10. **Double Click**: Buat tombol yang hanya bereaksi jika di-Double Click (`<Double-Button-1>`). Single click tidak melakukan apa-apa.

--- SULIT (5 Soal) ---
11. **Drag & Drop Sederhana**: Buat widget Label kecil (kotak warna). Implementasikan logic agar user bisa klik-tahan dan geser (drag) widget tersebut ke posisi mana saja dalam window. *Hint: Kombinasi `<Button-1>` dan `<B1-Motion>`, serta `.place()`*.
12. **Validasi Input Realtime**: Entry hanya menerima angka. Jika user ketik huruf, huruf tersebut langsung dihapus otomatis atau background entry jadi merah sejenak. Gunakan `trace_add` pada StringVar.
13. **Multiple Choice Quiz Generator**: Ada dictionary soal `{"Soal 1": ["A", "B", "C"], "Soal 2": ...}`. Generate Radiobutton secara dinamis menggunakan loop (bukan hardcode). Tombol "Cek Jawaban" menghitung skor.
14. **Custom Right Click Menu**: Buat menu popup yang muncul tepat di posisi kursor mouse saat user klik kanan di area window. (Materi Menu belum spesifik dibahas, tapi coba cari tentang `tk.Menu` dan method `.post()`).
15. **Keyboard Navigation Arrow**: Buat satu objek kotak (Label/Canvas rect). Gerakkan kotak tersebut ke atas/bawah/kiri/kanan menggunakan tombol panah keyboard.
"""
