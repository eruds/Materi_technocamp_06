# Problem 1
a = input("Masukkan bilangan A : ")
b = input("Masukkan bilangan B : ")
print(f"A yang dimasukkan adalah {a}")
print(f"B yang dimasukkan adalah {b}")
print("Hasil perkalian A dan B adalah ", a*b)

# Problem 2  
nama = input("Masukkan Nama : ")
usia = input("Masukkan Usia : ")
print("Halo, namaku " + nama + " dan usiaku " + usia + ".")

# Problem 3 
byte = int(input("Masukkan byte : "))
print(byte*8)

# Problem 4
dps = int(input("Masukkan kerusakan per detik : "))
length = int(input("Masukkan lamanya serangan : "))
damage = dps*length
posBuff = int(input("Masukkan buff positif : "))*damage//100
negBuff = int(input("Masukkan besar buff negatif : "))*damage//100
totalDamage = damage + posBuff - negBuff

print("Besar serangan : ", totalDamage)

# Problem 5 
# Asumsi penginputan nilai jam, menit, detik berdasarkan constraint 
jam = int(input("Masukkan jam pertama : "))
menit = int(input("Masukkan menit pertama : "))
detik = int(input("Masukkan detik pertama : "))
waktu1 = jam * 3600 + menit * 60 + detik 

jam = int(input("Masukkan jam kedua : "))
menit = int(input("Masukkan menit kedua : "))
detik = int(input("Masukkan detik kedua : "))
waktu2 = jam * 3600 + menit * 60 + detik 

diff = waktu2 - waktu1 
hours = diff // 3600 
minutes = ( diff - hours*3600 ) // 60
seconds = ( diff - hours*3600 - minutes * 60 ) 

print(f"Jumlah waktu kosong : {hours} jam {minutes} menit {seconds} detik")

# Using Functions 
def toSeconds(jam = 0, menit = 0, detik = 0) : 
    return jam * 3600 + menit * 60 + detik 

def getDiff(jam1, jam2) : 
    diff = jam2 - jam1
    hours = diff // 3600 
    minutes = ( diff - hours*3600 ) // 60
    seconds = ( diff - hours*3600 - minutes * 60 ) 
    return (hours, minutes, seconds)

jam = int(input("Masukkan jam pertama : "))
menit = int(input("Masukkan menit pertama : "))
detik = int(input("Masukkan detik pertama : "))
waktu1 = toSeconds(jam, menit, detik)

jam = int(input("Masukkan jam kedua : "))
menit = int(input("Masukkan menit kedua : "))
detik = int(input("Masukkan detik kedua : "))
waktu2 = toSeconds(jam, menit, detik)

diff = getDiff(waktu1, waktu2)
print(f"Jumlah waktu kosong : {diff[0]} jam {diff[1]} menit {diff[2]} detik")

# Using Class
class waktu: 
    def __init__(self, jam, menit, detik) : 
        self.jam = jam
        self.menit = menit
        self.detik = detik

    def __sub__(self, other):
        jam1 = self.toSeconds()
        jam2 = other.toSeconds()
        diff = jam1 - jam2
        hour = diff // 3600 
        minute = ( diff - hour*3600 ) // 60
        seconds = ( diff - hour*3600 - minute * 60 ) 
        return waktu(hour, minute, seconds)

    def __str__(self):
        return str(self.jam) + " jam " + str(self.menit) + " menit " + str(self.detik) + " detik" 
    
    def toSeconds(self)  : 
        return self.jam*3600 + self.menit*60 + self.detik

jam = int(input("Masukkan jam pertama : "))
menit = int(input("Masukkan menit pertama : "))
detik = int(input("Masukkan detik pertama : "))
waktu1 = waktu(jam,menit,detik)

jam = int(input("Masukkan jam kedua : "))
menit = int(input("Masukkan menit kedua : "))
detik = int(input("Masukkan detik kedua : "))
waktu2 = waktu(jam,menit,detik)

print(waktu2-waktu1)

