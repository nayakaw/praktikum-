def prima():   
    num = int(input("Masukkan bilangan: "))

    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num, "bukan bilangan prima")
                break
        else:
            print(num,"adalah bilangan prima")
    else:
        print(num, "bukan bilangan prima")

prima()