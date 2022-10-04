print("Menenentukan jenis segitiga")

sisiX=eval(input("Masukkan sisi X  "))
sisiY=eval(input("Masukkan sisi Y  "))
sisiZ=eval(input("Masukkan sisi Z  "))

if(sisiX == sisiY == sisiZ) :
    print("Merupakan jenis segitiga sama sisi")
elif(sisiX == sisiY) or (sisiY == sisiZ) or (sisiX == sisiZ):
    print("Merupakan jenis segitiga sama kaki")
else:
    print("Merupakan jenis segitiga sembarang")