celsius = float(input("Suhu Celsius\t: "))
reamur = (4/5) * celsius
fahrenheit = ((9/5) * celsius) + 32
kelvin = celsius + 273
print("Suhu Reamur\t:", reamur)
print("Suhu Fahrenheit\t:", fahrenheit)
print("Suhu Kelvin\t:", kelvin)

reamur = float(input("\nSuhu Reamur\t: "))
celsius = (5/4) * reamur
fahrenheit = ((9/4) * reamur) + 32
kelvin = ((5/4) * reamur) + 273
print("Suhu Celsius\t:", celsius)
print("Suhu Fahrenheit\t:", fahrenheit)
print("Suhu Kelvin\t:", kelvin)

fahrenheit = float(input("\nSuhu Fahrenheit\t: "))
celsius = (5/9) * (fahrenheit - 32)
reamur = (4/9) * (fahrenheit - 32)
kelvin = (5/9) * (fahrenheit - 32) + 273
print("Suhu Celsius\t:", celsius)
print("Suhu Reamur\t:", reamur)
print("Suhu Kelvin\t:", kelvin)

kelvin = float(input("\nSuhu Kelvin\t: "))
celsius = kelvin - 273
reamur = (4/5) * (kelvin - 273)
fahrenheit = (9/5) * (kelvin - 273) + 32
print("Suhu Celsius\t:", celsius)
print("Suhu Reamur\t:", reamur)
print("Suhu Fahrenheit\t:", fahrenheit)