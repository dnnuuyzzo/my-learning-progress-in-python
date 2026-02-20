"""
===============================================
LATIHAN PROYEK: TIC TAC TOE
===============================================
Game klasik X dan O
"""

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
    
    def tampilkan_papan(self):
        print("\n")
        for i in range(0, 9, 3):
            row = f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} "
            print(row)
            if i < 6:
                print("-----------")
        print(f"\nGiliran: {self.current_player}")
    
    def posisi_valid(self, pos):
        return 0 <= pos <= 8 and self.board[pos] == " "
    
    def buat_langkah(self, pos):
        if self.posisi_valid(pos):
            self.board[pos] = self.current_player
            return True
        return False
    
    def cek_pemenang(self):
        # Kombinasi kemenangan
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        
        for combo in wins:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] != " "):
                return self.board[combo[0]]
        return None
    
    def papan_penuh(self):
        return " " not in self.board
    
    def ganti_pemain(self):
        self.current_player = "O" if self.current_player == "X" else "X"
    
    def main(self):
        print("=" * 30)
        print("    TIC TAC TOE")
        print("=" * 30)
        print("Posisi papan:")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        
        while True:
            self.tampilkan_papan()
            
            try:
                pos = int(input("Pilih posisi (1-9): ")) - 1
            except ValueError:
                print("Masukkan angka 1-9!")
                continue
            
            if not self.buat_langkah(pos):
                print("Posisi tidak valid! Coba lagi.")
                continue
            
            pemenang = self.cek_pemenang()
            if pemenang:
                self.tampilkan_papan()
                print(f"\n🎉 Pemain {pemenang} MENANG!")
                break
            
            if self.papan_penuh():
                self.tampilkan_papan()
                print("\n🤝 SERI!")
                break
            
            self.ganti_pemain()

if __name__ == "__main__":
    game = TicTacToe()
    game.main()
