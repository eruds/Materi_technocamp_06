# def swap(i, j, arr):
#     temp = arr[i]
#     arr[i] = arr[j]
#     arr[j] = temp
#     return arr

# arr = [0,-41,9,-2,3,2, 53, 28]
# length = len(arr)
# # print(arr)
# for i in range(length) : 
#     for j in range(i,length) : 
#         print(arr)
#         if(arr[i] >= arr[j]) :
#             arr = swap(i, j, arr)
# print(arr)

# Insertion Sort 
arr = [0,-41,9,-2,3,2, 53, 28]
for i in range(1, len(arr)): 

    key = arr[i] 

    # Move elements of arr[0..i-1], that are 
    # greater than key, to one position ahead 
    # of their current position 
    j = i-1
    while j >= 0 and key < arr[j] : 
            arr[j + 1] = arr[j] 
            j -= 1
    arr[j + 1] = key 

print(arr)



# # Insertion Sort
# arr = [0,-41,9,-2,3,2, 53, 28]
# length = len(arr)
# def insert(i, x, arr) : 
#     print(arr[:i])
#     temp = arr[:i]
#     temp.append(x)
#     print(temp)
#     temp += arr[i:]
#     return temp

# flag = False

# for i in range(1,length) :
#     # print(arr)
#     for j in range(i-1,-1,-1) :
#         if(arr[i] > arr[j]) : 
#             arr = insert(j, arr[i], arr)
#             del arr[i+1]
#             flag = True
#         if(flag) : 
#             arr = insert(0, arr[i], arr)
#             del arr[i+1]
# # print(arr)