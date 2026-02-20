"""
MODUL 7: STRUKTUR OOP & FINAL PROJECT (BEST PRACTICES)
======================================================

Hingga saat ini kita coding dengan gaya prosedural (fungsi-fungsi).
Untuk aplikasi besar, WAJIB menggunakan Class (OOP) agar kode terorganisir.

A. STANDARD DIALOGS
-------------------
Tkinter menyediakan dialog bawaan:
- `messagebox`: (showinfo, showwarning, showerror, askyesno).
- `filedialog`: (askopenfilename, asksaveasfilename).
- `colorchooser`: (askcolor).

B. STRUKTUR CLASS TKINTER
-------------------------
Biasanya kita membuat class turunan dari `tk.Tk` atau `tk.Frame`.
```python
class AplikasiSaya(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App OOP")
        self.buat_widget()
```

"""

import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import os

class SimpleNoteApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Simple Note App (OOP Style)")
        self.geometry("600x400")
        
        # Setup UI
        self.setup_menu()
        self.setup_widgets()
        
    def setup_menu(self):
        menubar = tk.Menu(self)
        
        # Menu File
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.buka_file)
        file_menu.add_command(label="Save", command=self.simpan_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Menu Edit
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Clear Text", command=self.hapus_semua)
        edit_menu.add_command(label="Change Title", command=self.ganti_judul)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        # Menu Help
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.tampil_about)
        menubar.add_cascade(label="Help", menu=help_menu)
        
        self.config(menu=menubar)
        
    def setup_widgets(self):
        # Toolbar Frame
        toolbar = tk.Frame(self, bd=1, relief=tk.RAISED)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        tk.Button(toolbar, text="Open", command=self.buka_file).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(toolbar, text="Save", command=self.simpan_file).pack(side=tk.LEFT, padx=2, pady=2)
        
        # Status Bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        statusbar = tk.Label(self, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        statusbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Main Text Area
        # Frame untuk Text + Scrollbar
        frame_text = tk.Frame(self)
        frame_text.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(frame_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.text_area = tk.Text(frame_text, undo=True, yscrollcommand=scrollbar.set, padx=10, pady=10)
        self.text_area.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        
        scrollbar.config(command=self.text_area.yview)
        
    # --- LOGIC METHODS ---
    
    def buka_file(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return # User cancel
        
        self.text_area.delete(1.0, tk.END)
        try:
            with open(filepath, "r") as f:
                content = f.read()
                self.text_area.insert(tk.END, content)
            self.title(f"Simple Note App - {os.path.basename(filepath)}")
            self.status_var.set(f"File Opened: {filepath}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal membuka file: {str(e)}")

    def simpan_file(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
            
        try:
            content = self.text_area.get(1.0, tk.END)
            with open(filepath, "w") as f:
                f.write(content)
            self.title(f"Simple Note App - {os.path.basename(filepath)}")
            self.status_var.set(f"File Saved: {filepath}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan file: {str(e)}")

    def hapus_semua(self):
        if messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus semua teks?"):
            self.text_area.delete(1.0, tk.END)
            self.status_var.set("Text Cleared")

    def ganti_judul(self):
        judul_baru = simpledialog.askstring("Input", "Masukkan Judul Baru:")
        if judul_baru:
            self.title(judul_baru)

    def tampil_about(self):
        messagebox.showinfo("About", "Simple Note App\nDibuat sebagai Latihan Tkinter Modul 7")

if __name__ == "__main__":
    app = SimpleNoteApp()
    app.mainloop()

"""
===========================================================================
LATIHAN SOAL - BAGIAN 7 (FINAL PROJECT & STANDARD DIALOGS)
===========================================================================

--- MUDAH (5 Soal) ---
1. Tulis ulang kode dasar Tkinter ("Hello World") menggunakan pendekatan Class `class App(tk.Tk)`.
2. Buat tombol "Pilih Warna". Gunakan `colorchooser.askcolor()`. Ubah warna background window sesuai warna yang dipilih user.
3. Buat tombol "Simpan". Munculkan `messagebox.askyesno` "Apakah anda yakin?". Jika Yes print "Disimpan", jika No print "Batal".
4. Gunakan `simpledialog.askinteger` untuk meminta input umur user. Jika umur < 17, tutup aplikasi (`self.destroy`).
5. Buat program Text Viewer sederhana (Class-based) yang hanya punya tombol "Load File" dan Text Widget.

--- MENENGAH (5 Soal) ---
6. **File Size Checker**: Buat aplikasi kecil. Tombol "Pilih File" (filedialog). Setelah file dipilih, tampilkan Size file tersebut dalam KB/MB di Label.
7. **Directory Picker**: Gunakan `filedialog.askdirectory()`. Hitung jumlah file yang ada di dalam folder yang dipilih user dan tampilkan hasilnya.
8. **Login Class**: Buat Class `LoginForm` (turunan `tk.Frame` atau `tk.Toplevel`). Gunakan class ini di dalam window utama. Jika login sukses, `LoginForm` hilang, muncul konten utama.
9. **Kalkulator OOP**: Buat ulang kalkulator (penjumlahan/pengurangan) dengan struktur OOP. Pisahkan method `hitung` dan `setup_ui`.
10. **Form Validasi**: Saat tombol Save ditekan, lakukan validasi input. Jika ada data kosong, munculkan `messagebox.showwarning`. Jika semua benar, munculkan `messagebox.showinfo`.

--- SULIT (5 Soal) ---
11. **Image Gallery**: Aplikasi "Album Foto". 
    - Tombol "Open Folder" (`askdirectory`).
    - Load semua file .png/.gif di folder tersebut.
    - Tampilkan tombol "Next" dan "Prev" untuk navigasi gambar di Canvas/Label.
12. **CSV Editor Sederhana**:
    - Load file .csv.
    - Tampilkan datanya (bisa pakai banyak Entry di Grid atau Treeview jika mau explorasi sendiri).
    - Edit data.
    - Save kembali ke .csv.
13. **Simple Paint OOP**: 
    - Class `PaintApp`.
    - Canvas di tengah.
    - Toolbar di samping (Pilih Warna, Pilih Ukuran Brush, Penghapus).
    - Method `draw` yang bersih dan terorganisir.
14. **Settings Manager (JSON)**:
    - Aplikasi punya menu "Settings" -> Toplevel.
    - User ubah setting (misal font size, theme).
    - Saat Save, simpan setting ke `config.json`.
    - Saat aplikasi dibuka (``__init__``), load setting dari `config.json` agar preferensi user tersimpan.
15. **My Final Project**: Gabungkan semua ilmu! Buat aplikasi manajemen "Kontak Teman".
    - Simpan Nama, No HP, Alamat.
    - Data disimpan di File (TXT/JSON/CSV).
    - Bisa Tambah, Lihat List, Edit, Hapus.
    - Gunakan OOP, Validasi, dan Dialogs.
"""
