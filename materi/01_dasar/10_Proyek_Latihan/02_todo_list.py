"""
===============================================
LATIHAN PROYEK: TODO LIST
===============================================
Aplikasi manajemen tugas sederhana
"""

class TodoList:
    def __init__(self):
        self.tasks = []
    
    def tambah(self, tugas):
        self.tasks.append({"tugas": tugas, "selesai": False})
        print(f"✅ Tugas '{tugas}' ditambahkan!")
    
    def lihat(self):
        if not self.tasks:
            print("\n📋 Tidak ada tugas.")
            return
        
        print("\n" + "=" * 40)
        print("📋 DAFTAR TUGAS")
        print("=" * 40)
        
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["selesai"] else "○"
            print(f"{i}. [{status}] {task['tugas']}")
        
        belum = sum(1 for t in self.tasks if not t["selesai"])
        print(f"\nTotal: {len(self.tasks)} tugas, {belum} belum selesai")
    
    def selesaikan(self, nomor):
        if 1 <= nomor <= len(self.tasks):
            self.tasks[nomor - 1]["selesai"] = True
            print(f"✅ Tugas {nomor} ditandai selesai!")
        else:
            print("Nomor tugas tidak valid!")
    
    def hapus(self, nomor):
        if 1 <= nomor <= len(self.tasks):
            tugas = self.tasks.pop(nomor - 1)
            print(f"🗑️ Tugas '{tugas['tugas']}' dihapus!")
        else:
            print("Nomor tugas tidak valid!")

def main():
    todo = TodoList()
    
    while True:
        print("\n--- MENU ---")
        print("1. Lihat tugas")
        print("2. Tambah tugas")
        print("3. Tandai selesai")
        print("4. Hapus tugas")
        print("5. Keluar")
        
        pilihan = input("Pilihan: ")
        
        if pilihan == "1":
            todo.lihat()
        elif pilihan == "2":
            tugas = input("Tugas baru: ")
            todo.tambah(tugas)
        elif pilihan == "3":
            todo.lihat()
            nomor = int(input("Nomor tugas: "))
            todo.selesaikan(nomor)
        elif pilihan == "4":
            todo.lihat()
            nomor = int(input("Hapus nomor: "))
            todo.hapus(nomor)
        elif pilihan == "5":
            print("Sampai jumpa! 👋")
            break

if __name__ == "__main__":
    main()
