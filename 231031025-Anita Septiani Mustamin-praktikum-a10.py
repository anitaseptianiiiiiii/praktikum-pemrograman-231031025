#faktorial

def faktorial(nilai):
    if nilai <= 1:
        return 1
    else:
        return nilai * faktorial(nilai - 1)

# Program Utama
for i in range(11):
    print('%2d ! = %d' % (i, faktorial(i)))


def faktorial(nilai):
    if nilai <= 1:
        return 1
    else:
        return nilai * faktorial(nilai - 1)

# Meminta input 
nilai = int(input("Masukkan nilai untuk menghitung faktorial (misalnya 11): "))

# Memeriksa apakah nilai valid (misalnya, apakah nilai >= 0)
if nilai < 0:
    print("Maaf, faktorial untuk nilai negatif tidak didefinisikan.")
else:
    print("Hasil faktorial:")
    for i in range(nilai + 1):
        print('%2d ! = %d' % (i, faktorial(i)))
