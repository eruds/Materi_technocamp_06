# # Problem 1 
# n = int(input("Masukkan angka bilangan genap"))
# if ( n < 0 ) : 
#     print("n tidak boleh negatif")
# elif ( n == 0 ) : 
#     print()
# else : 
#     even = 0
#     for i in range(n) :
#         print(even)
#         even += 2

# # Problem 2 
# bil1 = int(input("Masukkan bilangan pertama: "))
# bil2 = int(input("Masukkan bilangan kedua: "))
# while bil1 + bil2 != 100:
#     print("Kedua bilangan tersebut tidak menghasilkan 100, ulangi!")
#     bil1 = int(input("Masukkan bilangan pertama: "))
#     bil2 = int(input("Masukkan bilangan kedua: "))
# print("Ya, jumlah kedua bilangan tersebut adalah 100")

# # Problem 3
# s = int(input("Masukkan S : "))
# if (s < 0 ) : 
#     print("S tidak boleh negatif!")
# else : 
#     for i in range(s) : 
#         for j in range(s) : 
#             print("*", end="")
#         print()

# # Problem 4
# n = int(input("Masukkan panjang alas dan tinggi : "))
# print("Hasil : ")
# if (n < 0 ) : 
#     print("S tidak boleh negatif!")
# else : 
#     for i in range(n) : 
#         for j in range(n) : 
#             if( j == 0 or j == i or i == n - 1) : 
#                 print("#", end="")
#             elif ( j < i): 
#                 print("*", end="")
#             else : 
#                 print(" ", end="")
#         print()

# # Problem 5 
# # 5.1 
# n = int(input("Masukkan n : "))
# sum = 0
# for i in range(n + 1) :
#     sum += i
# print(sum)

# n = int(input("Masukkan n : "))
# sum = 0 
# for i in range(n + 1) :
#     sum += i * i 
# print(sum)

# Problem 5.3 sama persis dengan problem 3
# Problem 5.4 dan 5.5 Sama persis dengan problem 4
# Bonus segitiga class 
class segitigaSiku : 
    def __init__(self, alas, tinggi) : 
        self.alas = alas 
        self.tinggi = tinggi
    def print(self) : 
        alas = self.alas 
        tinggi = self.tinggi 
        for i in range(tinggi) : 
            for j in range(alas) : 
                if ( i == tinggi - 1 ) :
                    print("*", end="")
                elif ( j <= i ): 
                    print("*", end="")
                else : 
                    print(" ", end="")
            print()
    def getArea(self) : 
        return self.alas * self.tinggi 
    
alas = int(input("Masukkan panjang alas: "))
tinggi = int(input("Masukkan tinggi : "))
segitigaSiku = segitigaSiku(alas, tinggi)
segitigaSiku.print()







