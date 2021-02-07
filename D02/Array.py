# List of Food
food = ["A Food", "Another Food", "A Whole Chicken", "A Pizza"]
# print(food)

# Empty List 
empty = []
# print(empty, len(empty))
empty.append("Not Empty Anymore")
# print(empty, len(empty))

# List with different Data Types 
aList = [True, "What", 10, 1.41, "Hello There", False, 92.53]
# print(aList)

# Merging Lists 
mergedList = food + empty 
# print(mergedList)
mergedList2 = empty + mergedList
# print(mergedList2)

# List With Range
rangedList = [i for i in range(10)]
# print(rangedList)



# An Array with 10 Elements
languages = [
    "C Sharp", "JavaScript", 
    "C++", "Ruby", "Kotlin", 
    "Java", "Haskell", "Prolog", 
    "SmallTalk", "Python"
]
# Accessing A List 
firstLang = languages[0]
# print(firstLang)
randomLang = languages[6]
# print(randomLang)

# print(languages[0])
# print(languages[3])
# print(languages[2:5])
# print(languages[4:-1]) # I Don't Know Why 
# print(languages[-1])
# print(languages)

# print(languages)

# Printing Using a for loop 
# for i in range( len(languages) ) : 
#     print(languages[i])

# for i in rangedList : 
#     print(i)

# # How to print the first letter on each language?
# for i in range(len(languages)) : 
#     print(languages[i][0])

# reverseRangedList = [i for i in range(10, 1, -1)]
# print(reverseRangedList)
# del reverseRangedList[0]
# print(reverseRangedList)
# del reverseRangedList[7]
# print(reverseRangedList)

# # Deleting an element 
# print(languages)
# del languages[1]
# # print(languages)
# languages.remove("Haskell")
# print(languages)

# Length of a languages 
# print(len(languages))





