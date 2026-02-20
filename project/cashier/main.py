import time
from datetime import datetime
from cashier_program import run_cashier_program
from system import clear_screen

now = int(datetime.now().strftime("%H"))
match now:
    case x if 5 < x <= 10: sapaan = "Pagi"
    case x if 10 < x <= 15: sapaan = "Siang"
    case x if 15 < x <= 19: sapaan = "Sore"
    case _: sapaan = "Malam"

while True:
    clear_screen()
    print(f"Selamat {sapaan}!")
    print("Pilih program yang ingin dijalankan:")
    print("  1. Program Kasir")        
    print("  2. Program Stok Barang")
    print("  0. Hentikan")

    try:
        input_user = int(input("Masukkan input = "))
        match input_user:
            case 0: break
            case 1:
                print("Menjalankan program, tunggu sebentar...")
                time.sleep(1.5)
                run_cashier_program()
                break
            case 2: 
                print("Program belum tersedia")
                time.sleep(1.5)
            case _:
                print("Pilihan tidak tersedia")
                time.sleep(1.5)

    except ValueError:
        print("Input harus berupa angka!")
        time.sleep(0.5)
        print("Memulai ulang...")
        time.sleep(1.5)

print("Program Terhenti")