# nama = input("Masukkan Nama : ")
# usia = input("Masukkan Usia : ")
# print("Halo, namaku " + nama + " dan usiaku " + usia + ".")

# byte = int(input("Masukkan byte : "))
# print(byte*8)

# dps = int(input("Masukkan kerusakan per detik : "))
# length = int(input("Masukkan lamanya serangan : "))
# damage = dps*length
# posBuff = int(input("Masukkan buff positif : "))*damage//100
# negBuff = int(input("Masukkan besar buff negatif : "))*damage//100
# totalDamage = damage + posBuff - negBuff


# print("Besar serangan : ", totalDamage)

a = float(input("Masukkan a : "))
b = float(input("Masukkan b : "))
c = float(input("Masukkan c : "))
determinan = b**2 - 4*a*c; 
if(determinan < 0 ) : 
    print("Akar-akarnya tidak ada")
else : 
    x1 = (-b + (determinan**(1/2))) / 2*a
    x2 = (-b - (determinan**(1/2))) / 2*a
    if ( x1 == x2 ) : 
        print(f"Akarnya cuma satu, yaitu : {x1}")
    else : 
        print(f"Akarnya ada dua {x1}, {x2}")
