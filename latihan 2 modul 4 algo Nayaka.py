print("Mencari jumlah hari dalam satu bulan")
repeat="y"
while repeat=="y":
    from calendar import monthrange
    year=int(input("Masukkan tahun: "))
    month=int(input("Masukkan bulan: "))
    days=monthrange(year,month) [1]
    print("di bulan itu terdapat",days,"hari")
    repeat=str(input("ketik y atau n untuk mengulang: "))
    print("/n")
    if repeat=="n":
        print("Terima kasih telah menggunakan program ini")