n = int(input("Masukkan N : "))
arr = []
for i in range(n) :
    x = int(input()) 
    arr.append(x)
print(f"Hasil : {arr}")

# Sum
Sum = 0
for i in range(len(arr)) : 
    Sum += arr[i]
# Rata-rata 
avg = Sum / len(arr)
# Nilai Maksimal 
max = float("-inf")
for i in arr : 
    if(i > max) : 
        max = i 
# Nilai Minimal 
min = float("inf")
for i in range(len(arr)) : 
    item = arr[i]
    if( item < min) : 
        min = item
print(f"Sum : {Sum}")
print(f"Max : {max}")
print(f"Min : {min}")
print(f"Avg : {avg}")

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