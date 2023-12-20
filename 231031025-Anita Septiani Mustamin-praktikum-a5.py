
#a = True

#while a :
#    print('Menjalankan Program')

#kode ini adalah cara menjalankan program perulangan. Namun, belum selesai karena terjadi perulangan secara terus menerus.



a = True                                                            #merupakan variabel dengan nilai True
PERULANGAN = 0                                                      #merupakan variabel dengan nilai =0
while a:                                                            #memulai perulangan while yang akan terus berjalan selama nilai a=True
    if PERULANGAN >= 5 :                                            #Baris ini memeriksa apakah nilai perulangan lebih besar dari atau sama dengan 5
        print  ('Program selesai')                                  #Baris ini mencetak string "Program selesai"
        a = False                                                   #membuat nilai a menjadi False yang akan membuat perulangan while berhenti
    else:                                                           # Baris ini dieksekusi jika kondisi dalam pernyataan if tidak terpenuhi
        PERULANGAN += 1                                             #Baris ini menambahkan nilai perulangan sebesar 1
        print ('Menjalankan program sebanyak', PERULANGAN, 'kali')  #Baris ini mencetak string "Menjalankan program sebanyak ", diikuti oleh nilai perulangan, diikuti oleh string "kali"

