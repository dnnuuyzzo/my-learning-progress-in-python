"""
MODUL 5: WIDGET LANJUTAN (TEXT, LISTBOX, SCROLLBAR, COMBOBOX)
=============================================================

Di modul ini kita akan menangani input teks multi-baris, daftar pilihan (list), dan dropdown.
Widget ini memerlukan penanganan khusus, terutama scrollbar.

A. TEXT WIDGET
--------------
Untuk input teks multi-baris (seperti Notepad).
- Insert text: `.insert(index, string)`
- Ambil text: `.get(start_index, end_index)` -> Contoh: `.get("1.0", tk.END)`
- Index format: "baris.karakter" (1-based untuk baris, 0-based untuk karakter). "1.0" = Baris 1, huruf ke-0.

B. LISTBOX
----------
Untuk menampilkan daftar item teks.
- Insert: `.insert(index, item)` -> `.insert(tk.END, "Item Baru")`
- Ambil yang dipilih: `.curselection()` mengembalikan tuple index yang dipilih.

C. SCROLLBAR
------------
Widget Scrollbar harus "dihubungkan" secara manual ke widget target (Text/Listbox).
- Widget Target: set parameter `yscrollcommand = scrollbar.set`
- Scrollbar: set parameter `command = widget.yview`

D. COMBOBOX (Dropdown)
----------------------
Berada di modul `tkinter.ttk` (Themed Tkinter). Lebih modern dari `OptionMenu`.
- Set values: `combobox['values'] = list_data`
- Get value: `.get()`

"""

import tkinter as tk
from tkinter import ttk # Import module ttk untuk Combobox
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.title("Widget Lanjutan - Bagian 5")
    root.geometry("700x500")

    # --- 1. COMBOBOX ---
    frame_combo = tk.LabelFrame(root, text="Pilih Data (Combobox)", padx=10, pady=10)
    frame_combo.pack(pady=10, padx=10, fill=tk.X)

    lbl_buah = tk.Label(frame_combo, text="Pilih Buah:")
    lbl_buah.pack(side=tk.LEFT)

    # Values bisa definisikan langsung
    data_buah = ["Apel", "Jeruk", "Mangga", "Pisang", "Anggur"]
    combo_buah = ttk.Combobox(frame_combo, values=data_buah, state="readonly") 
    # state="readonly" agar user tidak bisa mengetik text sembarangan, hanya pilih.
    combo_buah.pack(side=tk.LEFT, padx=10)
    combo_buah.current(0) # Pilih index ke-0 secara default

    def ambil_pilihan():
        pilihan = combo_buah.get()
        messagebox.showinfo("Info", f"Anda memilih: {pilihan}")

    btn_pilih = tk.Button(frame_combo, text="Pilih", command=ambil_pilihan)
    btn_pilih.pack(side=tk.LEFT)


    # --- 2. LISTBOX DAN SCROLLBAR ---
    # Kita butuh Frame penampung agar Scrollbar menempel rapi di samping Listbox
    frame_list = tk.LabelFrame(root, text="Daftar Item (Listbox + Scrollbar)", padx=10, pady=10)
    frame_list.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Buat Scrollrbar dulu
    scrollbar_list = tk.Scrollbar(frame_list)
    scrollbar_list.pack(side=tk.RIGHT, fill=tk.Y)

    # Buat Listbox
    # selectmode: SINGLE (satu), MULTIPLE, EXTENDED (pakai Ctrl/Shift)
    listbox = tk.Listbox(frame_list, height=6, yscrollcommand=scrollbar_list.set)
    
    # Isi data dummy (banyak baris agar scrollbar muncul)
    for i in range(1, 51):
        listbox.insert(tk.END, f"Item Data Nomor {i}")
        
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Hubungkan balik scrollbar ke listbox
    scrollbar_list.config(command=listbox.yview)

    def hapus_item():
        # curselection me-return TUPLE indices, misal (2,) atau (0, 2, 5)
        selected_indices = listbox.curselection()
        if not selected_indices:
            return # Tidak ada yg dipilih
        
        # Hapus dari index TERBESAR dulu agar index yg lebih kecil tidak bergeser
        for index in reversed(selected_indices):
            listbox.delete(index)

    btn_hapus = tk.Button(root, text="Hapus Item Terpilih", command=hapus_item, bg="#e74c3c", fg="white")
    btn_hapus.pack(pady=5)


    # --- 3. TEXT AREA ---
    frame_text = tk.LabelFrame(root, text="Catatan (Text Widget)", padx=10, pady=10)
    frame_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    
    txt_catatan = tk.Text(frame_text, height=5, width=40)
    txt_catatan.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Text widget juga perlu scrollbar jika isinya panjang (opsional di sini kita skip scrollbar demo)
    
    def baca_catatan():
        # "1.0" = Baris 1, char 0.
        # "end-1c" = Sampai akhir dikurangi 1 char (karena Text widget auto nambah newline di akhir)
        isi = txt_catatan.get("1.0", "end-1c") 
        print(f"Isi Catatan:\n{isi}")
        print("-" * 20)

    btn_baca = tk.Button(root, text="Print Catatan ke Console", command=baca_catatan)
    btn_baca.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()

"""
===========================================================================
LATIHAN SOAL - BAGIAN 5 (ADVANCED WIDGETS)
===========================================================================

--- MUDAH (5 Soal) ---
1. Buat Combobox sederhana berisi nama-nama hari (Senin-Minggu). Tambahkan tombol yang jika diklik menampilkan hari yg dipilih di Label.
2. Buat widget Text (Note) dengan ukuran width=30, height=10. Isi default text "Tulis disini..." saat program jalan (Gunakan `.insert()`).
3. Buat Listbox berisi 5 nama temanmu.
4. Buat Listbox dan tombol "Hapus Semua". Jika tombol diklik, Listbox menjadi kosong (`.delete(0, tk.END)`).
5. Buat program Text Widget yang memiliki tombol "Clear". Tombol ini menghapus seluruh tulisan di Text area.

--- MENENGAH (5 Soal) ---
6. **To-Do List Sederhana**: Ada Entry untuk input tugas, tombol "Add", dan Listbox penampung tugas. Tugas yang diketik masuk ke Listbox.
7. **Text Counter**: Text widget dengan Label di bawahnya yang menunjukkan jumlah karakter yang sudah diketik (Gunakan Binding event `<KeyRelease>`).
8. **Linked Combobox**: Buat 2 Combobox. Box 1: "Makanan", "Minuman". Jika dipilih "Makanan", Box 2 isinya ["Nasi", "Roti"]. Jika "Minuman", Box 2 isinya ["Air", "Teh"]. (Event `<<ComboboxSelected>>`).
9. **Scrollable Text**: Buat Text widget yang memiliki Scrollbar Vertikal. Text widget harus bisa discroll dengan mouse wheel maupun drag bar.
10. **Pindah Item**: Dua Listbox berdampingan (Kiri & Kanan). Tombol ">>" memindahkan item terpilih dari Kiri ke Kanan. Tombol "<<" sebaliknya.

--- SULIT (5 Soal) ---
11. **Text Editor Mini**: 
    - Menu File -> Open/Save.
    - Text Area utama.
    - Fitur Open: Membaca file `.txt` (gunakan `filedialog` - coba cari/preview materi ini dikit) dan menampilkannya di Text Area.
    - Fitur Save: Menyimpan isi Text Area ke file `.txt`.
12. **Search Listbox**: Ada Entry "Cari" di atas Listbox. Listbox berisi 50 nama kota. Saat user mengetik di Entry, isi Listbox terfilter secara realtime menampilkan kota yang cocok saja.
13. **Multi-Select & Delete**: Listbox dengan mode `selectmode=tk.MULTIPLE` atau `tk.EXTENDED`. User bisa pilih banyak item sekaligus (shift/ctrl click) lalu tekan tombol Hapus untuk menghapus semuanya sekaligus. *Pastikan loop penghapusan benar (reversed)*.
14. **Log Viewer**: Text widget dalam mode `state='disabled'` (Read Only). Buat fungsi `log(pesan)` yang:
    - Mengaktifkan state normal.
    - Menulis pesan di baris paling bawah.
    - Auto scroll ke paling bawah (`.see(tk.END)`).
    - Mematikan state `disabled` lagi.
    Gunakan tombol simulasi untuk menambah log.
15. **Form Input Kompleks**: 
    - Entry Nama.
    - Combobox Jabatan.
    - Text Area Alamat.
    - Checkbox Skill (Python, Java, C++).
    - Tombol "Submit" mengumpulkan semua data itu menjadi satu string format JSON/Dict dan menampilkannya di Messagebox.
"""
