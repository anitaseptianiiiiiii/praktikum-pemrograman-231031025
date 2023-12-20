#a = True                             #variabel dengan nilai True

#while a:                             # Mulai perulangan while yang akan terus berjalan selama nilai a=True
#    pilih = input('Pilihan: ')       # Meminta pengguna untuk memasukkan input dan menyimpannya dalam variabel pilih. Input ini akan digunakan untuk menentukan jalannya program.
#    if pilih == 'ya':                # Melakukan pengecekan apakah input yang dimasukkan oleh pengguna adalah string 'ya'.
#        print('Selamat Datang')      # Program akan mencetak "Selamat datang".
#    elif pilih == 'tidak':           # Jika input tidak sama dengan 'ya', maka dilakukan pengecekan apakah input tersebut adalah string 'tidak
#        print('Sampai Jumpa')        # Program akan mencetak 'sampai jumpa'


a = True                              # Variabel dengan nilai True

while a:                              # Memulai perulangan while yang akan terus berjalan selama nilai a=True
    pilih = input('Pilihan: ')        # Meminta pengguna untuk memasukkan input dan menyimpannya dalam variabel pilih. Input ini akan digunakan untuk menentukan jalannya program.
    if pilih == 'ya':                 # Melakukan pengecekan apakah input yang dimasukkan oleh pengguna adalah string 'ya'.
        print('Selamat Datang')       # Program akan mencetak "Selamat datang".
        a = False                     # Membuat nilai a menjadi False yang akan membuat perulangan while berhenti
    elif pilih == 'tidak':            # Jika input tidak sama dengan 'ya', maka dilakukan pengecekan apakah input tersebut adalah string 'tidak
        print('Sampai Jumpa')         # Program akan mencetak 'sampai jumpa'
        a = False                     # Membuat nilai a menjadi False yang akan membuat perulangan while berhenti
    else :                            # Baris ini dieksekusi jika kondisi dalam pernyataan if tidak terpenuhi
        continue                      # Melanjutkan terus program
