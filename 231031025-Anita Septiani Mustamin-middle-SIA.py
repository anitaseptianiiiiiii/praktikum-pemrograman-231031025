''' UTS
1. Buat variabel jenis list berikut.
    
    Bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu hasil studi mahasiswa',
            'Nama Lengkap',
            'NIM',
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil',
            'aktif',
            'Tanggal-Bulan-Tahun Lahir']
#(NOTED: sesuaikan dengan data anda)


2. Buat variabel nested list berikut.

MK =   [['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [3,2,3,2,3,3,3,2],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [3.50,3.00,3.75,4.00,3.75,3.50,3.75,3.00]]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, dan Nilai)

3. Buat Kode dengan hasil runing seperti berikut.


            INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                           JURUSAN SAINS
                    KARTU HASIL STUDI MAHASISWA
                          GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : NIM
Program/Prodi   : S1/Sistem Informasi A
Tahun Masuk     : 2023-Ganjil
Status          : Aktif
|--|--   12   --|--             31            --|-- 7 --|--    13   --|
-----------------------------------------------------------------------
No. Kode        |           Mata Kuliah         |  SKS  | Nilai (0-4) |
-----------------------------------------------------------------------
1   22A1209     | Matkul1                       |   3   |         3.50|
2   22A1210     | Matkul2                       |   2   |         3.00|
3   22A1211     | Matkul3                       |   3   |         3.75|
4   22A1212     | Matkul4                       |   2   |         4.00|
5   22A1213     | Matkul5                       |   3   |         3.75|
6   22A1214     | Matkul6                       |   3   |         3.50|
7   22A1215     | Matkul7                       |   3   |         3.75|
8   22A1216     | Matkul8                       |   2   |         3.00|
-----------------------------------------------------------------------
                                       TOTAL SKS:   21
-----------------------------------------------------------------------
|---------------------------------71-----------------------------------|
Summary:
Jumlah Mata Kuliah : 8 Mata Kuliah
Nilai Tertinggi    : 4.00  (22A1212 - Matkul4)
Nilai Terendah     : 3.00  (22A1211 - Matkul2)
IP Kumulatif       : 3.00
                                   
                                               Parepare, 25 Oktober 2023



                                                     NAMA LENGKAP      
                                                     ------------
'''



# Tulis Kode Jawaban di bawah!
Bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu hasil studi mahasiswa',
            'Anita Septiani Mustamin',
            '231031025',
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil',
            'aktif',
            '21 September 2005']

MK =   [['Kalkulus Dasar I','Pengantar Pemrograman','Wawasan Cinta IPTEK dan IMTAQ','Pancasila','Agama Islam','Pengantar Teknologi Informasi','Bahasa Indonesia','Sains Terpadu'],
        [3,3,2,2,2,3,2,3],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [3.50,3.00,3.75,4.00,3.75,3.50,3.75,3.00]]

kampus = Bio[0].upper().center(71)
jurusan = Bio[2].upper().center(71)
kartu = Bio[3].upper().center(71)
tahun = f'{Bio[9].upper()} {Bio[8]}'.center(71)

print(kampus)
print(jurusan)
print(kartu)
print(tahun)
print()

nama_lengkap = f'{Bio[4].upper()}'
nim = Bio[5]
program = Bio[7]
tahun = Bio[8][0:4]
status = Bio[10]

# Data biodata
nama_lengkap, nim, program, tahun, status 

# Data khs
matakuliah, sks, kode_matakuliah,nilai=MK
print(f'Nama Lengkap      : {nama_lengkap}\nNIM               : {nim}\nProgram/prodi     : {program}\nTahun Masuk       : {tahun}\nStatus            : {status.title()}\n')
print('-'*71)
print("|{:^2}| {:<11}| {:<30} |  {:<4} |  {:<10}|".format("No.", "Kode", "Mata Kuliah", "SKS", "Nilai (0-4)"))
print("-" * 71)
for i in range(len(matakuliah)):
    print("|{:^2} |{:<11} | {:<30} |  {:<4} |  {:<10} |".format(i + 1, kode_matakuliah[i], matakuliah[i], sks[i], nilai[i]))
print("-" * 71)

# Menghitung total SKS
total_sks = sum(sks)
print(f"{'TOTAL SKS:':^60}   {total_sks}")
print("-" * 71)

print("Summary:")
print(f"Jumlah Mata Kuliah : {len(matakuliah)} Mata Kuliah")
print(f"Nilai Tertinggi    : {max(nilai):.2f}  ({kode_matakuliah[nilai.index(max(nilai))]} - {matakuliah[nilai.index(max(nilai))]})")
print(f"Nilai Terendah     : {min(nilai):.2f}  ({kode_matakuliah[nilai.index(min(nilai))]} - {matakuliah[nilai.index(min(nilai))]})")
print(f"IP Kumulatif       : {sum(nilai) / len(nilai):.2f}")
print("\n")
print(f"{Bio[1].rjust(59)},25 Oktober 2023\n\n")
print(f"{nama_lengkap.upper().rjust(71)}")