"""
===============================================
LATIHAN PROYEK: KALKULATOR
===============================================
Proyek latihan untuk mengasah pemahaman dasar Python
"""

def kalkulator():
    print("=" * 40)
    print("       KALKULATOR SEDERHANA")
    print("=" * 40)
    print("Operasi: +, -, *, /, **, %")
    print("Ketik 'keluar' untuk berhenti")
    print("=" * 40)
    
    while True:
        try:
            input1 = input("\nAngka pertama: ")
            if input1.lower() == 'keluar':
                break
            
            operator = input("Operator (+,-,*,/,**,%): ")
            input2 = input("Angka kedua: ")
            
            a = float(input1)
            b = float(input2)
            
            if operator == '+':
                hasil = a + b
            elif operator == '-':
                hasil = a - b
            elif operator == '*':
                hasil = a * b
            elif operator == '/':
                if b == 0:
                    print("Error: Pembagian dengan nol!")
                    continue
                hasil = a / b
            elif operator == '**':
                hasil = a ** b
            elif operator == '%':
                hasil = a % b
            else:
                print("Operator tidak valid!")
                continue
            
            print(f"Hasil: {a} {operator} {b} = {hasil}")
            
        except ValueError:
            print("Error: Masukkan angka yang valid!")

if __name__ == "__main__":
    kalkulator()
