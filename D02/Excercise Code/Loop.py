# Problem 1 
n = int(input("Masukkan angka bilangan genap"))
if ( n < 0 ) : 
    print("n tidak boleh negatif")
elif ( n == 0 ) : 
    print()
else : 
    even = 0
    for i in range(n) :
        print(even)
        even += 2

bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))
while bil1 + bil2 != 100:
    print("Kedua bilangan tersebut tidak menghasilkan 100, ulangi!")
    bil1 = int(input("Masukkan bilangan pertama: "))
    bil2 = int(input("Masukkan bilangan kedua: "))
print("Ya, jumlah kedua bilangan tersebut adalah 100")
