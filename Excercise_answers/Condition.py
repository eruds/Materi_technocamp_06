# Problem 1
# Cara 1 
num = int(input("Masukkan bilangan: "))
if( num < 0 ) : 
    if(num % 2 == 0) : 
        print(f"{num} adalah bilangan positif genap")
    else : 
        print(f"{num} adalah bilangan positif ganjil")
elif ( num > 0 ) : 
    if(num % 2 == 0) : 
        print(f"{num} adalah bilangan negatif genap")
    else : 
        print(f"{num} adalah bilangan negatif ganjil")
else : 
    print("Input adalah bilangan 0")

# Dengan hanya menggunakan fungsi 
def isEven(num) : 
    return num % 2 == 0

def isPostive(num) : 
    return num > 0

def problem1(num) : 
    # Menggunakan shorthand if 
    pos = "positif" if isPostive(num) else "negatif"
    even = "genap" if isEven(num) else "ganjil"
    # OR 
    # pos = "positif" if num % 2 == 0 else "negatif"
    # even = "genap" if num > 0 else "ganjil"
    if(num != 0) :
        print(f"{num} adalah bilangan {pos} {even}")
    else : 
        print("Input adalah bilangan nol")
        
num = int(input("Masukkan bilangan: "))
problem1(num)

# Problem 2 
nilai = int(input("Masukkan Nilai: "))

# Bisa menggunakan pengulangan
# while(nilai > 100 or nilai < 0) : 
#     print("Nilai tidak valid!")
#     nilai = int(input("Masukkan Nilai: "))

# Bisa menggunakan range 
# if( nilai not in range(0,100)) : 

if(nilai > 100 or nilai < 0) : 
    if( 80 <= nilai <= 100 ) : 
        print("Indeks A!")
    elif( 73 <= nilai <= 79 ) : 
        print("Indeks AB!")
    elif( 65 <= nilai <= 72 ) : 
        print("Indeks B!")
    elif( 57 <= nilai <= 64 ) : 
        print("Indeks BC!")
    elif( 50 <= nilai <= 56 ) : 
        print("Indeks C!")
    elif( 35 <= nilai <= 49 ) : 
        print("Indeks D!")
    else : 
        print("Indeks E!")

# Problem 3 
num = int(input("Masukkan bilangan: "))
if( num % 6 == 0 ) : 
    print(f"{num} adalah kelipatan 6")
else : 
    print(f"{num} bukan kelipatan 6")

# Dengan menggunakan fungsi 
def kelipatan(target, num) :
    answer = "adalah" if num % 6 == 0 else "bukan"
    print(f"{num} {answer} kelipatan {target}")


# Problem 4
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


# dengan menggunakan class 
class quadraticEquation : 
    def __init__(self, a, b, c) : 
        self.a = a
        self.b = b
        self.c = c
    def __str__(self) : 
        return str(a) + "x^2 + " + str(b) + "x + " + str(c)
    def __add__(self,other) : 
        return quadraticEquation(
            self.a + other.a, 
            self.b + other.b, 
            self.c + other.c
        )
    def roots(self) : 
        # We usually will return a value rather than a printed information 
        # determinan = b**2 - 4*a*c; 
        # if(determinan < 0 ) : 
        #     print("Akar-akarnya tidak ada")
        # else : 
        #     x1 = (-b + (determinan**(1/2))) / 2*a
        #     x2 = (-b - (determinan**(1/2))) / 2*a
        #     if ( x1 == x2 ) : 
        #         print(f"Akarnya cuma satu, yaitu : {x1}")
        #     else : 
        #         print(f"Akarnya ada dua {x1}, {x2}")
        # Returning a value 
        determinan = b**2 - 4*a*c; 
        if(determinan < 0 ) : 
            return False
        else : 
            x1 = (-b + (determinan**(1/2))) / 2*a
            x2 = (-b - (determinan**(1/2))) / 2*a
            return  {"x1" : x1, "x2" : x2} if x1 != x2 else {"x1" : x1}

a = float(input("Masukkan a : "))
b = float(input("Masukkan b : "))
c = float(input("Masukkan c : "))
func = quadraticEquation(a, b, c)
roots = func.roots()
if(roots) : 
    if ( len(roots) == 1 ) : 
        print(f"Akarnya cuma satu, yaitu : {roots['x1']}")
    else : 
        print(f"Akarnya ada dua {roots['x1']}, {roots['x2']}")
else : 
    print("Akar-akarnya tidak ada")