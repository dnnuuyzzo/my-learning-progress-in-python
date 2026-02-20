with open("Tes.txt", "r+") as file:
    for i in range(10):
        file.write(f"{i+1}, {i+2}, {i+3}\n")
    file.seek(0)
    for i in range(10):
        x, y, z = file.readline().replace(" ", "").split(",")
        print(x, y, z)