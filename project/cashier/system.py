import os

DATABASE_PRODUK = "database_produk.txt"
LIST_NAMA_BARANG = []
LIST_HARGA = []
LIST_STOK = []

def clear_screen():
    if os.name == "nt": os.system('cls')
    else: os.system('clear')

def list_produk(nama_barang, harga, stok):
    LIST_NAMA_BARANG.append(nama_barang)
    LIST_HARGA.append(harga)
    LIST_STOK.append(stok)