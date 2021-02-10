# Problem 1 
nomor_telepon = [0,8,1,2,3,4,5,6,7,8,9,0]
print("Nomor Telepon : ", nomor_telepon)
sum = 0;
for i in nomor_telepon:
    sum += i
print("Hasil Enkripsi : ", sum)

# Problem 2
n = int(input("Masukkan N : "))
if n >= 0 : 
    arr = []
    for i in range(n) :
        x = int(input()) 
        arr.append(x)
    print("Hasil : ", arr)
else : 
    print("N tidak boleh negatif!")

# Problem 3 
# Without array 
n = int(input("Masukkan N : "))
if n >= 0 : 
    max = float("-inf")
    for i in range(n) :
        x = int(input()) 
        max = x if x > max else max 
    print("NIlai Maksimum : ", max)
else : 
    print("N tidak boleh negatif!")
# With array 
n = int(input("Masukkan N : "))
if n >= 0 : 
    arr = []
    for i in range(n) :
        x = int(input()) 
        arr.append(x)
    max = float("-inf")
    for i in arr : 
        max = i if i > max else max 
    if len(arr) > 0 : 
        print("Nilai Maksimum : ", max)
else : 
    print("N tidak boleh negatif!")


# Problem 4 with File read 
data = []
file = open("datakotabandung.txt", "r", encoding="utf-8")
with open("datakotabandung.txt", "r", encoding="utf-8") as file : 
    for line in file : 
        line = float(line.strip())
        data.append(line)
print(data)
sum = 0
max = float("-inf")
min = float("inf") 
for i in range(len(data)) : 
    sum += data[i]
    # print(sum)
    if(data[i] > max) : 
        max = data[i]
    if(data[i] < min) : 
        min = data[i]    
avg = sum/len(data)
print(f"Max : {max}")
print(f"Min : {min}")
print(f"Avg : {avg}")

# Problem 5 
# Problem 5.1 
n = int(input("Masukkan N : "))
if n >= 0 : 
    arr = []
    for i in range(n) :
        x = int(input()) 
        arr.append(x)
    result = []
    for i in arr : 
        if ( i > 90 ) : 
            result.append("A")
        elif( 81 > i >= 90 ) :
            result.append("B")
        elif ( 71 > i >= 80 ) : 
            result.append("C")
        else : 
            result.append("D")
    print("Daftar Nilai adalah sebagai berikut: ",result)
else : 
    print("N tidak boleh negatif!")

# Dengan fungsi 
def inputArray(n) : 
    if n >= 0 : 
        arr = []
        for i in range(n) :
            x = int(input()) 
            arr.append(x)
        return arr 
    else : 
        print("N tidak boleh negatif!")

def filterArr(arr) : 
    result = []
    for i in arr : 
        if ( i > 90 ) : 
            result.append("A")
        elif( 81 > i >= 90 ) :
            result.append("B")
        elif ( 71 > i >= 80 ) : 
            result.append("C")
        else : 
            result.append("D")
    return result

n = int(input("Masukkan N : "))
arr = inputArray(n)
result = filterArr(arr)
print(result)

# Problem 5.2 : dengan class
class ArrOfInt : 
    def __init__(self, arr = []) : 
        self.__arr = arr 
        self.lenght = len(self.arr)
    def __str__(self) : 
        sentence = "["
        for i in range(self.lenght):
            if( i == self.lenght - 1 ) : 
                sentence += self.arr[i]
            else : 
                sentence += self.arr[i] + ", "
        return sentence + "]"
    def append(self, num) : 
        self.arr.append(num)
        self.length += 1
    
    def getValues(self) : 
        return self.__arr

    def inputArray(self, n) : 
        if n >= 0 : 
            arr = []
            for i in range(n) :
                x = int(input()) 
                self.arr.append(x)
        else : 
            print("N tidak boleh negatif!")
    def max(self) : 
        arr = self.arr
        max = float("-inf")
        for i in arr :
            max = i if i > max else max
        return max 
    def min(self) :
        arr = self.arr
        mim = float("inf")
        for i in arr :
            min = i if i < min else min
        return min

n = int(input("Masukkan N : "))
arrOfInt = arrOfInt()
arrOfInt.append(n)
print("Nilai Max : ", arrOfInt.max())
print("Nilai Min : ", arrOfInt.min())

# Problem 5.3 
# Dengan function 
def sumArr(arr) : 
    sum = 0
    for i in range(len(arr)) : 
        sum += arr[i]
    return sum 

def sumArrAlternate(arr) :
    sum = 0
    for i in range(len(arr)) : 
        if(i % 2 == 0) : 
            sum -= arr[i]
        else : 
            sum += arr[i]
    return sum 

def addToAllElements(arr, num) : 
    for i in range(len(arr)) : 
        arr[i] += num 
    return arr 


n = int(input("Masukkan N : "))
arrOfInt = ArrOfInt()
arrOfInt.append(n)

arrSum = sumArr(arrOfInt.getValues())
arrAlt = sumArrAlternate(arrOfInt.getValues())
addValue = addToAllElements(arrOfInt.getValues, 10)

print(arrSum)
print(arrAlt)
print(addValue)

# Problem 5.4 with function 
def multArr(arr1, arr2) : 
    if(len(arr1) != len(arr2)) : 
        raise Exception("Multiplied array cant be on different dimensions")
    else : 
        temp = []
        for i in range(len(arr1)):
            temp.append(arr1[i] * arr2[i])
    return temp 

# Cara 1 
def addArray(arr1, arr2) : 
    return arr1 + arr2

# Cara 2 
def addArray(arr1, arr2) :
    temp = [] 
    length = len(arr1) + len(arr2)
    for i in range(length) : 
        if(i < len(arr1)): 
            temp.append(arr1[i])
        else : 
            temp.append(arr2[i])
    return temp 

# Problem 5.5 There's a way to use classes but i'm just to lazy to do it so let's just do the easy way okay 
def getRow(mat, row) : 
    return mat[row]

def getCol(mat, col) : 
    temp = []
    for arr in mat : 
        temp.append(arr[col])
    return temp

def addMatrix(mat1, mat2) :
    row1 = len(mat1)
    col1 = len(mat1[0])
    row2 = len(mat2)
    col2 = len(mat2[0])
    temp = []
    if ( row1 != row2 or col1 != col2 ) : 
        for i in range(row1): 
            row = []
            for j in range(col1) :
                row.append(mat1[i][j] + mat2[i][j])  
            temp.append(row)
        return temp 
    else : 
        raise Exception("Invalid matrix")

# def multMatrix(mat1, mat2) : 
#     row1 = 

matrix1 = [
    [1,2,4],
    [2,1,4], 
    [6,4,1]
]

matrix2 = [
    [5,6,7],
    [1,2,8], 
    [0,8,1]
]
