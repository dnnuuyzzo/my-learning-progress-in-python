"""
MODUL 6: KANVAS GRAFIS & GAMBAR (CANVAS & IMAGES)
=================================================

Widget `Canvas` adalah area serbaguna untuk menggambar bentuk geometris, menempatkan gambar, 
membuat grafik, hingga membuat animasi game sederhana.

A. SISTEM KOORDINAT CANVAS
--------------------------
Canvas menggunakan koordinat X (Horizontal) dan Y (Vertikal).
- Titik (0, 0) berada di POJOK KIRI ATAS.
- X bertambah ke Kanan.
- Y bertambah ke Bawah (Perhatikan ini beda dengan diagram Cartesius matematika biasa).

B. MENGGAMBAR BENTUK (PRIMITIVES)
---------------------------------
- `.create_line(x1, y1, x2, y2, ...)`
- `.create_rectangle(x1, y1, x2, y2)`
- `.create_oval(x1, y1, x2, y2)` -> Membuat lingkaran/elips di dalam kotak pembatas.
- `.create_text(x, y, text="...")`
- `.create_image(x, y, image=...)`

C. MEMINDAHKAN OBJEK (ANIMASI)
------------------------------
- `.move(item_id, dx, dy)`: Memindahkan objek sejauh dx, dy.
- `.coords(item_id, ...)`: Mengubah koordinat objek.

"""

import tkinter as tk
from tkinter import messagebox
import time

def main():
    root = tk.Tk()
    root.title("Canvas & Graphics - Bagian 6")
    root.geometry("600x600")

    # Membuat Canvas
    canvas = tk.Canvas(root, width=500, height=400, bg="white", highlightthickness=1, highlightbackground="black")
    canvas.pack(pady=20)

    # --- 1. MENGGAMBAR BENTUK ---
    
    # GARIS (Line)
    # Dari (50, 50) ke (200, 50). fill=warna, width=ketebalan
    line = canvas.create_line(50, 50, 200, 50, fill="blue", width=3)
    
    # KOTAK (Rectangle)
    # Pojok kiri-atas (50, 100), Pojok kanan-bawah (200, 200)
    rect = canvas.create_rectangle(50, 100, 200, 200, fill="#e74c3c", outline="black")
    
    # LINGKARAN/OVAL
    # Didefinisikan berdasarkan kotak pembatas (Bounding Box)
    # Untuk membuat lingkaran sempurna, lebar dan tinggi kotak harus sama
    oval = canvas.create_oval(250, 50, 350, 150, fill="yellow", outline="orange", width=2)
    
    # TEKS
    text_obj = canvas.create_text(300, 200, text="Halo Canvas!", font=("Arial", 14, "bold"), fill="purple")

    
    # --- 2. TAGS & BINDING ---
    # Kita bisa memberi "tag" pada objek canvas untuk menyeleksinya nanti
    canvas.create_oval(400, 50, 450, 100, fill="green", tags="bola_hijau")
    
    def klik_bola(event):
        messagebox.showinfo("Canvas", "Bola Hijau diklik!")
        
    # Binding event KLIK pada objek spesifik yang punya tag "bola_hijau"
    canvas.tag_bind("bola_hijau", "<Button-1>", klik_bola)


    # --- 3. ANIMASI SEDERHANA ---
    
    # Mari kita buat bola merah untuk dianimasikan
    # Start di posisi (50, 300), ukuran 30x30
    ball = canvas.create_oval(50, 300, 80, 330, fill="red")
    
    def gerakkan_kanan():
        # .move(item, dx, dy)
        # dx=10 (geser kanan 10px), dy=0 (tidak gerak vertikal)
        canvas.move(ball, 10, 0)
        
        # Cek posisi sekarang
        pos = canvas.coords(ball) # returns [x1, y1, x2, y2]
        print(f"Posisi Bola: {pos}")

    btn_gerak = tk.Button(root, text="Gerak Kanan >>", command=gerakkan_kanan)
    btn_gerak.pack(pady=5)
    
    
    # --- 4. GAMBAR EXTRENAL (IMAGES) ---
    # Tkinter hanya support PNG dan GIF secara native (JPG butuh library Pillow/PIL)
    # Karena kita tidak tahu apakah user punya file gambar, kita buat gambar dummy dari data base64
    # atau skip bagian ini.
    # Code contoh:
    # img_file = tk.PhotoImage(file="path/to/image.png")
    # c_img = canvas.create_image(100, 100, image=img_file, anchor="nw")
    # PENTING: Variabel `img_file` harus disimpan (Keep Reference) agar tidak di-Garbage Collect python.

    tk.Label(root, text="Klik Bola Hijau atau Gunakan Tombol Gerak").pack()

    root.mainloop()

if __name__ == "__main__":
    main()

"""
===========================================================================
LATIHAN SOAL - BAGIAN 6 (CANVAS)
===========================================================================

--- MUDAH (5 Soal) ---
1. Buat Canvas ukuran 400x300 dengan background hitam.
2. Gambar sebuah garis diagonal dari pojok kiri atas ke pojok kanan bawah canvas. Warnanya putih.
3. Gambar "Bendera Jepang" sederhana (Kotak putih besar, lingkaran merah di tengah).
4. Buat objek teks di tengah canvas bertuliskan "GAME OVER" dengan font besar dan warna merah.
5. Buat sebuah kotak biru. Tambahkan tombol "Hapus" yang jika diklik menghapus kotak tersebut (`canvas.delete(item_id)`).

--- MENENGAH (5 Soal) ---
6. **Traffic Light**: Gambar kotak hitam panjang vertikal. Di dalamnya gambar 3 lingkaran (Merah, Kuning, Hijau) secara vertikal.
7. **Bouncing Ball Logic**: Buat bola. Buat tombol "Step". Setiap diklik, bola bergerak 10px ke kanan. Jika koordinat x2 bola > lebar canvas, bola harus bergerak ke kiri (pantul manual logic).
8. **Mouse Drawing**: Buat fitur "Paint" sederhana. Saat user klik dan geser mouse (`<B1-Motion>`), gambar lingkaran-lingkaran kecil di posisi mouse event.x, event.y sehingga membentuk garis coretan.
9. **Draggable Object**: Buat kotak persegi. Implementasikan logic agar kotak ini bisa didrag (digeser) menggunakan mouse.
10. **Random Stars**: Gunakan loop untuk menggambar 50 titik (oval kecil 2x2px) berwarna putih di posisi acak (random x,y) pada canvas background hitam, menyerupai langit berbintang.

--- SULIT (5 Soal) ---
11. **Analog Clock UI**: Gambar lingkaran jam. Gunakan rumus trigonometri (sin/cos) untuk menggambar garis jarum jam, menit, detik (statis dulu, menunjuk ke jam 3 misalnya).
12. **Basic Animation Loop**: Tanpa tombol. Bola bergerak otomatis dari kiri ke kanan. Gunakan `root.after(ms, function_name)` untuk membuat loop animasi yang smooth.
13. **Collision Detection**: Buat dua kotak. Satu kotak diam, satu kotak digerakkan dengan tombol keyboard (W/A/S/D). Jika kotak bergerak menabrak/menyentuh kotak diam, ubah warna kotak diam jadi merah. *Hint: `canvas.coords(item)`*.
14. **Image Viewer**: Tampilkan sebuah gambar (PNG) di canvas. Tambahkan tombol Zoom In (Perbesar) dan Zoom Out (Perkecil) yang mengubah ukuran gambar (Ini agak tricky di Tkinter murni tanpa PIL untuk resize, tapi coba cari tahu method `zoom` atau `subsample` pada PhotoImage).
15. **Game Tangkap Bola (Konsep)**: Bola jatuh dari atas ke bawah secara otomatis. Di bawah ada "Papan" (persegi panjang) yang bisa digerakkan kiri-kanan oleh user. Jika bola menyentuh papan, skor bertambah dan bola reset ke atas. Jika lewat, Game Over.
"""
