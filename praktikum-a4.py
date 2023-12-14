import os
os.system('clear')

nim = ['2','3','1','0','3','1','0','1','7']
#nim2 = '231031017'
print(nim[1:3])
#print(nim2[1:3])
print()

#akses item
print('----------Akses Item Positif----------')
print(f'item index o : {nim[0]}')
print(f'item index 4 : {nim[4]}')
print(f'item index terakhir : {nim[len(nim)-1]}')
print()

#akses item negatif
print('----------Akses Item Negatif----------')
print(f'item index terakhir : {nim[-1]}')
print(f'item index pertama : {nim[-len(nim)]}')
print(f'item index  6 : {nim[-5]}')
print(f'item index  4 : {nim[-6]}')
print(f'item index  7 : {nim[-2]}')
print()

#akses index batas
print('----------Akses Index Batas----------')
print(f'item index  1,2.....: \n {nim[1:]}')
print(f'item index  3,4.....: \n {nim[3:]}')
print(f'item index  0,1,2   : \n {nim[:3]}')
print(f'item index  0,1,2,3 : \n {nim[:4]}')
print(f'item index  semua : \n {nim[:]}')
print(f'item index  [:8] : \n {nim[:-1]}')
print(f'item index  [:6] : \n {nim[:-3]}')
print()

#pengirisan
print('----------Pengirisan Index----------')
print(f'item index  1,2 : \n {nim[1:3]}')
print(f'item index  2,3,4: \n {nim[2:5]}')
print(f'item index  kosong : \n {nim[3:3]}')
print(f'item index  [8:8] kosong : \n {nim[-1:-1]}')
print(f'item index  [1:8] kosong : \n {nim[1:-1]}')
print(f'item index  [2:7] kosong : \n {nim[2:-2]}')
print()
 
#latihan list
print('----------Tugas List----------')
data = ['Indra Wahyulla',2023,'Aktif']
nilai= [90,89,93,97]

print('Nama\t: '+ data[0])
print('angkatan:', data[1])
print('status\t: '+ data[2])
print()

print(f'{data[0]} Status Kuliah\t: {data[2]}')
print(f'Data terbesar nilai adalah\t: {max(nilai)}')
print(f'Data terkecil nilai adalah\t: {min(nilai)}')
print(f'Data terbesar nilai adalah\t: {sum(nilai)/len(nilai)}')
print()

#latihan tupple
print('----------Tugas Tupple----------')
data = ('Indra Wahyulla',2023,'Aktif')
nilai= (90,89,93,97)

print(data[1])
print(data[-1])
print(nilai[1:-1])
print()

print(f'Jumlah nilai {data[0]} adalah: {len(nilai)}')
print(f'Data terbesar nilai adalah\t: {max(nilai)}')
print(f'Data terkecil nilai adalah\t: {min(nilai)}')
print(f'Data terbesar nilai adalah\t: {sum(nilai)/len(nilai)}')
print()

#latihan nestedlist

print('----------Tugas Nested List----------')
data = [['Indra Wahyulla',2023,'Aktif'],
        [90,89,93,97],
        [20,22],
        ['S1-Reguler','Ganjil'],[231031017]]
print(data)
print()

#tugas 1 : tambahkan matkul dan sks
kelas = [('kalkulus',2),
         ('pemrograman',3)]
print(kelas)
kelas.append(('pancasila',3))
kelas.append(('Sainster',3))
kelas.append(("PTI",2))
print(kelas)
print()

#output
#Mata kuliah 1 : Matkul 1 dengan jumlah sks 2
print(f"Mata Kuliah 1: {kelas[0][0]} dengan {kelas[0][1]} sks")
#Mata kuliah 2 : Matkul 1 dengan jumlah sks 3
print(f"Mata Kuliah 2: {kelas[1][0]} dengan {kelas[1][1]} sks")
#Mata kuliah 3 : Matkul 1 dengan jumlah sks 3
print(f"Mata Kuliah 3: {kelas[2][0]} dengan {kelas[2][1]} sks")
#Mata kuliah 4 : Matkul 1 dengan jumlah sks 2
print(f"Mata Kuliah 4: {kelas[3][0]} dengan {kelas[3][1]} sks")
print()

print(data[0][0])
print(data[-1][0])
print(data[2][0:])
print()

# >> Tugas : nama mahasiswa thomas dengan nim : 88888888
print(f'nama mahasiswa {data[0][0]}   dengan nim : {data[4][0]}')
# >> program pendidikan thomas : s1-reguler
print(f'program pendidikan {data[0][0]} : {data[3][0]}')
print()

print(f'Program Pendidikan {data[0][0]}\t: {data[3][0]}')
print(f'Angkatan\t: {data[0][1]}-{data[3][1]}')
print(f'jumlah Nilai {data[0][0]} Adalah\t: {len(data[1])}')
print(f'Data terbesar nilai {data[0][0]} adalah\t: {max(nilai)}')
print(f'Data terbesar nilai {data[0][0]} adalah\t: {min(nilai)}')
print(f'Data terbesar nilai {data[0][0]} adalah\t: {sum(nilai)/len(nilai)}')