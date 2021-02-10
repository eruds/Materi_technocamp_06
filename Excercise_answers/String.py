# Problem 1
name = input("Masukkan nama : ")
print(f"Halo {name}, semoga harinya menyenangkan")

# Problem 2
sentence = input("Masukkan kalimat : ")
print("Banyaknya huruf : ", len(sentence))

# Problem 3
word = input("Masukkan kata : ")
vocal = ["a", "i", "u", "e", "o", "A", "I", "U", "E", "O"]

# The python way 
if ( word[0] in vocal ) : 
    print("Huruf pertama merupakan huruf vokal")
else : 
    print("Huruf pertama bukan huruf vokal")

# General Programming way 
flag = False 
firstLetter = word[0]
i = 0 
while flag and i < len(vocal) : 
    if(firstLetter == vocal[i]) : 
        flag = True 
    i += 1 

# Problem 4 
# With reverse 
word = input("Masukkan kata : ")
reverse = word[::-1]
if(word == reverse) : 
    print(f"{word} merupakan sebuah palindrom")
else : 
    print(f"{word} bukan sebuah palindrom") 

# Dengan loop 
# Not the best implementation 
i = 0
j = len(word) - 1
flag = False 
if (j % 2 == 0 ) : 
    while j - i == 1 and flag: 
        if(word[i] != word[j]) : 
            flag = True 
        i += 1
        j -= 1 
else : 
    while i != j and flag: 
        if(word[i] != word[j]) : 
            flag = True 
        i += 1
        j -= 1 


# Dengan reverse for loop function  
def reverseWord(word) : 
    reverse = ""
    for i in range(len(word), 0, -1): 
        reverse += word[i]
    return reverse

def checkPalindrome(word) : 
    return reverseWord(word) == word

def problem4(word) : 
    verdict = "merupakan" if checkPalindrome(word) else "bukan"
    print(f"{word}, {verdict} sebuah palindrom")

word = input("Masukkan kata : ")
problem4(word)