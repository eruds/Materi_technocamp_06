x = -10 
y = 20 
z = 30 
if ( x > y ) : 
    if ( y > z ) : 
        print("Terurut mengecil")
elif ( x < y ) : 
    if ( y < z ) : 
        print("Terurut Membesar")
else : 
    print("Tidak keduanya")

# First Example
x = 20 
y = 10 
if( x > y ) : 
    print("X is larger than Y")
elif ( x < y ) : 
    print("Y is larger than X")
else : 
    print("X is equal to Y")


# String Length 
print(len("Hello World!"))

# First Letter 
print("Hey There"[5])

# Modulo 
if(10 % 2 == 0 ) : 
    print(True)
else : 
    print(False)
print(True if (10 % 2 == 0 ) else False)
print(10 % 2 == 0)

# Second Example
print("Masukkan bilangan ke-1: ")
A = int(input())
print("Masukkan bilangan ke-2: ")
B = int(input())
print("Masukkan bilangan ke-3: ")
C = int(input())

if ((A < B) and (B < C)) :
    print("Ketiga bilangan tersebut terurut membesar.")
elif ((A > B) and (B > C)) :
    print("Ketiga bilangan tersebut terurut mengecil.")
else :
    print("Ketiga bilangan tersebut tidak terurut membesar ataupun mengecil.")

# Tenary Operator
x = "Is Bigger" if 10 > 20 else "Is Lower"
y = "Is Bigger" if 20 > 30 else "Is Lower" if 20 < 30 else 20 == 20
print(x)
print(y)

# Third Example
print("Tahun berapakah yang ingin Anda cek? ")
A = int(input())

# if (A % 4 == 0) :
#     if (A % 100 == 0) :
#         if (A % 400 == 0) :
#             print("Tahun tersebut merupakan tahun kabisat")
#         else :
#             print("Tahun tersebut bukan tahun kabisat")
#     else :
#         print("Tahun tersebut merupakan tahun kabisat")
# else :
#     print("Tahun tersebut bukan tahun kabisat")
