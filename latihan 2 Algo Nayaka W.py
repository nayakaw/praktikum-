print('Hitung Luas Ruangan')
p = float(input('Masukkan Panjang Ruangan: '))
l = float(input('Masukkan Lebar Ruangan: '))
satuan = input("Masukkan satuan (Meter/Inci):  ")
luas = p*l
print('Luas Ruangan dengan panjang', p ,'dan lebar', l , 'adalah %.1f'%luas, satuan)