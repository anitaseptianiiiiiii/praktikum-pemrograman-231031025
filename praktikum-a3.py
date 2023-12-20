print("praktikum-a3\n\n")
nama = 'anita septiani mustamin'
nim = '231031025'
meet = 'praktikum 3'
prodi = 'sistem informasi A'
email = 'anditanuu@gmail.com'
sp = 40
prodi = 'Sistem Informasi'
TTL = 'Parepare, 21 September 2005'
alamat = 'Jl. Messang Bau Massepe No.23'
asal = 'Parepare'
hobi = 'Traveling'
tinggi = '163cm'

print ('-'*sp)
print (f'{nama.upper().center(sp)}')
print (f'{nim.center(sp)}\n\n')
print (f'{meet.capitalize().rjust(sp)}')
print (f'{prodi.title().rjust(sp)}')
print (f'{email.rjust(sp)}')
print ('-'*sp)

print(f'\tHalo, nama saya {nama.title()} dengan NIM {nim} dari prodi {prodi.title()}. Ini adalah file {meet.capitalize()}. Terima kasih.')

print (f'''Biodata saya:
Nama\t : {nama.title()}
Prodi\t : {prodi.title()}
NIM\t : {nim}
TTL\t : {TTL}
Alamat\t : {alamat}
Asal\t : {asal}
Hobi\t : {hobi}
Tinggi\t : {tinggi}
''')

stat = 'Newton Frankel Isaac'
up   = stat.upper()
print (up)
up = up.split() #up menjadi list n item
print (up)
print(up[-1][0],' '.join(up[0:-1]))
print ('F SIR ISAAC NEWTON')

print (up[-1], up [0][0], up [1][0])
print ('NEWTON S I')

print ()

stat2 = '&sir$ @isaac# *newton.'
up2   = stat2.upper()
print (up2)
up2   =up2.split()
print (up2)
print (up2[0][1:-1], up2[1][1:-1], up2 [2][1:-1])
print (up2[0].strip('&$'),up2[1].strip('@#'),up2[2].strip('*.'))
print ('SIR ISAAC NEWTON')

print ('===============TUGAS PRAKTIKUM 3===============')
print('Tugas Praktikum 3'.center(35))
nama = 'Anita Septiani Mustamin'
nim  = '231031025'
prodi= 'Sistem Informasi A'
print(f'''
Nama\t: {nama}
NIM\t: {nim}
prodi\t: {prodi}''')


'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outpunya sesuai'''


str1 = 'duFort Frankel Von Neumann'
up = str1.upper().split(" ")
print(up[-1]," ".join(up[0:3]))
#output: NEUMANN DUFORT FRANKEL VON

str2 = 'duFort Frankel Von Neumann'
up2 = str1.upper().split(" ")
print(f'{up2[0][0]}{up2[1][0]}{up2[2][0]} {up2[3]}')
#output: DFV NEUMANN

str3 = 'duFort Frankel Von Neumann'
up3 = str1.upper().split(" ")
print(f'{up3[0]} {up3[1][0]}{up3[2][0]}{up3[3][0]}')
#output: DUFORT FVN

str4 = 'duFort Frankel Von Neumann'
up4 = str4.upper().split(" ")
print(f'{up4[3][0]} {str4[0:6]} {up4[1][0]}{up4[2][0]}')
#output: N duFort FV

str5 = 'duFort Frankel Von Neumann'
up5 = str4.lower().split(" ")
print(f'{up5[-1].upper()} {up5[0][0]} {up5[1][0]} {up5[2][0]}')
#output: NEUMANN d f v
str6 = 'duFort Frankel Von Neumann'
up5 = str4.upper().split(" ")
print(f'{up5[-1]} {up5[0][0]}{up5[1][0]}{up5[2][0]}')
#output: NEUMANN DFV

str7 = '@duFort Frankel Von Neumann$'
up7 = str7.split(" ")
print(f'{up7[0].strip("@")} {up7[1]} {up7[2]} {up7[3].upper().strip("$")}')
#output: duFort Frankel Von NEUMANN

str8 = '#duFort4Frankel4Von4Neumann$'
up8 = str8.split("4")
print(f'{up8[0].strip("#")} {up8[1]} {up8[2]} {up8[3].strip("$")}')
#output: duFort Frankel Von Neumann

str9 = '@duFort@-^Frankel*-(Von(-(Neumann$'
up9 = str9.split("@")
up92= up9[2].split("-") 
print(f'{up9[1]} {up92[1].strip("^*")} {up92[2].strip("(")} {up92[3].strip("($")}')
#output: duFort Frankel Von Neumann

str10 = '@DUFort@1^FraNkel*1(VoN(1(NeuMann^'
up10 = str10.split("1")
print(up10[0][1:-1].lower().replace('f','F'), up10[1][1:-1].title(), up10[2][1:-1].title(), up10[3][1:-1].title())
#output: duFort Frankel Von Neumann
