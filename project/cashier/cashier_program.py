from system import *
import time

header_1 = "SELAMAT DATANG DI TOKO BAROKAH 354"
header_2 = "Selamat Berbelanja ^_^"
alamat = "JALAN PAHLAWAN NO. 123"
keranjang_barang = []
harga_sementara = 0
input_user_stok = 0
input_user_barang = 0

def run_cashier_program():
    global harga_sementara
    global keranjang_barang
    global input_user_barang, input_user_stok
    global isEmpty

    while True:
        LIST_NAMA_BARANG.clear()
        LIST_HARGA.clear()
        LIST_STOK.clear()
        clear_screen()

        print("="*100)
        print(f"{header_1:^100}")
        print(f"{alamat:^100}")
        print("-"*100)
        print(f"{header_2:^100}")
        print("="*100)

        print(f"{"No":^3} | {"Nama Barang":^58} | {"Harga":^20} | {"Stok":^10}")
        print("="*100)

        try:
            with open(DATABASE_PRODUK, "r") as file:
                cek_produk = file.readlines()
                if not cek_produk:
                    isEmpty = True
                    print(f"\n{"Belum Ada Produk":^100}\n")
                    print("="*100)
                    print('Isi produkmu di menu "TAMBAH PRODUK" di file ...')
                    file.close()
                else:
                    isEmpty = False
                    file.seek(0)
                    for index, baris in enumerate(file):
                        if baris.strip():
                            nama_barang, harga, stok = baris.strip().split(",")
                            if not nama_barang:
                                nama_barang = "-"
                            if not harga:
                                harga = "0"
                            if not stok:
                                stok = "0"

                            list_produk(nama_barang, harga, stok)
                            print(f"{index + 1:^3} | {nama_barang:58} | {"Rp." + harga:^20} | {stok + " pcs":^10}")
                            time.sleep(0.1)

                    print(f"{"0":^3} | {"Selesai dan Bayar":58} | {"":^20} | {"":^10}")
            
        except FileNotFoundError:
            with open(DATABASE_PRODUK, "w") as file:
                print(f"\n{"Belum Ada Produk":^100}\n")
                print("="*100)
                print('Isi produkmu di menu "TAMBAH PRODUK" di file ...')

        print("="*100)
        if not keranjang_barang: pass
        else:
            if input_user_stok == 0: pass
            else: 
                print("Keranjang\t: ", end= "")
                print(", ".join(keranjang_barang).lower()) 
                print(f"Total Sementara\t: Rp.{harga_sementara}")
                print("="*100)

        if isEmpty == False:
            try:
                input_user_barang_str = input("Pilih Nomor Produk yang Diinginkan\t: ")
                input_user_barang = int(input_user_barang_str)
                if input_user_barang == 0: 
                    print(f"\033[A\033[41C Berhenti")
                    break
                elif input_user_barang > len(LIST_NAMA_BARANG) or input_user_barang < 0:
                    print(f"\033[A\033[41C {input_user_barang} (Barang Tidak Tersedia)")
                    time.sleep(1)
                    continue

            except ValueError:
                print(f"\033[A\033[41C {input_user_barang_str} (Input harus berupa angka)")
                time.sleep(1)
                continue

        print(f"\033[A\033[41C {input_user_barang} ({str(LIST_NAMA_BARANG[input_user_barang - 1])})")
        nama_barang_pilihan = LIST_NAMA_BARANG[input_user_barang - 1]
        harga_pilihan = int(LIST_HARGA[input_user_barang - 1])
        
        while True:
            try:
                input_user_stok_str = input("Masukkan Jumlah Produk yang Diinginkan\t: ")
                input_user_stok = int(input_user_stok_str)
                break
            except ValueError:
                print(f"\033[A\033[41C {input_user_stok_str} (Input harus berupa angka)")
                time.sleep(1)
                print("\033[A\033[2K", end="")
                continue
            
        print(f"\033[A\033[41C {input_user_stok} pcs")
        
        if input_user_stok > int(LIST_STOK[input_user_barang - 1]):
            print("Stok tidak mencukupi")
            time.sleep(1)
        elif input_user_stok < 0:
            print("Jumlah Tidak Valid!")
            time.sleep(1)
        else:
            harga_sementara += (harga_pilihan * input_user_stok)
            keranjang_barang.append(f"{input_user_stok} pcs {nama_barang_pilihan}")
            stok_lama = int(LIST_STOK[input_user_barang - 1])
            stok_baru = stok_lama - input_user_stok
            LIST_STOK[input_user_barang - 1] = str(stok_baru)
            with open(DATABASE_PRODUK, "r") as file:
                baris = file.readlines()
                target_nama = LIST_NAMA_BARANG[input_user_barang - 1]
                target_harga = LIST_HARGA[input_user_barang - 1]
                baris[input_user_barang - 1] = f"{target_nama},{target_harga},{stok_baru}\n"

            with open(DATABASE_PRODUK, "w") as file:
                file.writelines(baris)


if __name__ == "__main__":
    while True:
        run_cashier_program()
        break 