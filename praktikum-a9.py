def judul():
    print('PROGRAM MENGHITUG LUAS DAN KELILING '.center(45))
    print('BANGUN DATAR PERSEGI'.center(45))
    print()

def inputan():
    panjang=float(input('masukkan panjang: '))
    lebar=float(input('masukkan lebar: '))
    return panjang,lebar 

def luasan(panjang,lebar):
    hasil= panjang*lebar
    return hasil

def keliling(panjang,lebar):
    hasil = (panjang,lebar)*2

def tampil(pesan,nilai):
    print(f'hasil perhitungan nilai {pesan}: {nilai}')

def pilihan():
    pilih=input('apakah ingin lanjut: [y/n]')
    if pilih == 'y':
        a=True
    else:
        a=False
        print('sampai jumpa')



a=True
while a:
    #judul
    judul()
    #inputan 
    panjang,lebar=inputan()
    #luas
    luas=luasan(panjang,lebar)
     #keliling
    keliling=keliling(panjang,lebar)
     #cetak
    tampil('luas',luas)
    tampil('keliling',keliling)
     #pilihan
    a=pilihan()