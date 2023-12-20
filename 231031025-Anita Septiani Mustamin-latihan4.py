('LATIHAN 4')
pendapatan = int(input('Masukkan besaran pendapatan : '))

if pendapatan <= 0 and pendapatan <=1000:
    persentase = 0
elif pendapatan <= 1001 and pendapatan <=2000:
    persentase = 10
elif pendapatan <= 2001 and pendapatan <=3000:
    persentase = 20
elif pendapatan <= 3001 and pendapatan <=4000:
    persentase = 30
elif pendapatan <= 4001 and pendapatan <=5000:
    persentase = 40
else:
    persentase = 50

#Menghitung nilai variabel bonus 
bonus = (pendapatan * persentase) / 100
#Menghitung jumlah total pendapatan 
total = pendapatan + bonus

print('Besar Pendapatan : ', pendapatan)
print('Besar Persentase : ', str(persentase)+'%')
print('Bonus : ', bonus)
print('Total Pendapatan : ', total)