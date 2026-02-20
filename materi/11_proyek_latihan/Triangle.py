sisi = 10
count = 0
mid = sisi
for i in range(sisi * 2):
    if i % 2 != 0:
        print(" " * mid ,"+" * count)
        mid -= 1
    
    count += 1