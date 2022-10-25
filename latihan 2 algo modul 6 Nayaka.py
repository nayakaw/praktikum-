
print("Program menentukan jumlah hari dalam bulan tertentu")

F = False

year = ''

#Fungsi tidak berparameter
def Kabisat(year):
    if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
        print("29 hari dalam sebulan")
    else:
        print("28 hari dalam sebulan")
    
#Fungsi berparameter
def NonKabisat(bulan):
    if bulan in [0,1,2,3,4,5,6,7,8,9,10,11,12]:
        if bulan in [4,6,9,11]:
            print("30 hari dalam sebulan")
        elif bulan in [1,3,5,7,8,10,12]:
            print("31 hari dalam sebulan")
        elif bulan == 2:
            year = int(input("Masukkan tahun (e.g., 2021): "))
            Kabisat(year) #Melempar Nilai ke dalam fungsi berparameter
    else:
        print("Error")

while (not F):
    print("Masukkan 0 untuk menghentikan program")
    bulan = int(input("masukkan bulan (1-12): "))
    if bulan == 0:
        F = True
    else:
        NonKabisat(bulan) #Melempar Nilai ke dalam fungsi berparameter
        
print("Terima kasih telah menggunakan program ini, sampai berjumpa lagi")