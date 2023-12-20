#Fungsi Rekursif Fibonacci
#def fibonacci(n):
#    if n<0:
#        print('Tidak ada bilangan yang bernilai negatif')
#    if n==0 or n==1:
#        return n
#    else:
#        return fibonacci(n-1) + fibonacci(n-2)
#Program Utama
#hasil=fibonacci(20)
#print('Fibonacci(%d)=%d' % (nilai,hasil))


def fibonacci(n):
    if n < 0:
        print('Tidak ada bilangan yang bernilai negatif')
        return None
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Meminta input dari pengguna
nilai = int(input("Masukkan nilai untuk mencari deret Fibonacci (misal 20): "))

# Mengecek dan mencetak nilai Fibonacci jika nilai valid
if nilai >= 0:
    hasil = fibonacci(nilai)
    print('Fibonacci(%d) = %d' % (nilai, hasil))
else:
    print("Maaf, nilai yang dimasukkan tidak valid untuk deret Fibonacci.")
