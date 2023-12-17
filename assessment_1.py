# #           #Programmes
#
# # Print a String in reverse
#
# # Method-1
# string = "String to be reversed"
# print(string[::-1])
#
# # Method-2
# string = "String to be reversed"
# rev = reversed(string)
# res = [i for i in rev]
# st = "".join(res)
# print(st)
#
# # Method-3
# string = "String to be reversed"
# res = ""
# for character in string:
#     res = character + res
#
# print(res)
#
# ############################################################################################################
#
# # String Palindrome
# def palindrome(string):
#     if string == string[::-1]:
#         print("Yes Its a Palindrome")
#     else:
#         print("NO Its not a Palindrome")
#
# palindrome("gadag")
# palindrome("Moolya")
#
# ############################################################################################################
#
# # File Handling
# file = open(r"./try.txt", 'r')
#
# for each in file:
#     print (each)
# ##################################
#
# file = open(r"./try.txt", "r")
# print(file.read())
# ##################################
#
# with open(r"./try.txt") as file:
#     data = file.read()
#
# print(data)
# ##################################
#
# file = open(r"./try.txt", "r")
# print(file.read(5))
# ##################################
#
# with open(r"./try.txt", "r") as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split()
#         print(word)
# ##################################
#
# file = open(r"./try.txt",'w')
# file.write("This is the write command")
# file.write("It allows us to write in a particular file")
# file.close()
#
# ##################################
# file = open(r"./try.txt", 'a')
# file.write("This will add this line")
# file.close()
#
#
# ############################################################################################################
# # Count the occurrence of unique words in a file
# path = r"./try.txt"
# with open(path) as file:
#     read_file = file.read().lower()
#     words = read_file.split()
#     word_count = {}
#
#     for word in words:
#         if word not in word_count:
#             word_count[word] = 1
#         else:
#             word_count[word] += 1
#
#     res = []
#     for key, value in word_count.items():
#         if value == 1:
#             res.append(key)
#     print(res)

# with open("try.txt", "w") as file:
#     file.write("moolya was created with a goal in mind to provide\n"
#                "well written well thought and well\n"
#                "explained solutions for\n"
#                "selected questions moolya")
#     file.close()
#
# ############################################################################################################
# Two input String is Anagram
# def anagrams(sen1, sen2):
#     # the sorted strings are checked
#     if (sorted(sen1) == sorted(sen2)):
#         print("The strings are anagrams.")
#     else:
#         print("The strings aren't anagrams.")
#
# sen1 = "listen"
# sen2 = "silent"
# anagrams(sen1, sen2)
#
#
# # ############################################################################################################
# Sort by Alphabets
# l = ["a", "b", "c", "d", "A", "B", "C", "D"]
# print(sorted(l))

# ##################################
# lst = ['Stem', 'constitute', 'Sedge', 'Eflux', 'Whim', 'Intrigue']
# res = sorted(lst)
# print(res)

# ##################################
# res = sorted(lst, key=str.lower)
# print(res)

# ##################################
# res = sorted(lst, reverse=True)
# print(res)
#
# ##################################
# res = sorted(lst, key=str.lower, reverse=True)
# print(res)
#
# x = [3,2,1]
# x.sort()
# print(x)
#
# x = [3,2,1]
# res = sorted(x)
# print(x)
# print(res)
#
# # ############################################################################################################
#
# List, Tuples, Dictionaries
# A list is mutable i.e we can make any changes in the list.
# The list allows duplicate elements
# [1, 2, 3, 4, 5]

# A tuple is immutable i.e we can not make any changes in the tuple.
# Tuple allows duplicate elements
# (1, 2, 3, 4, 5)

# A dictionary is mutable, But Keys are not duplicated.
# The dictionary doesn’t allow duplicate keys.
# {1: “a”, 2: “b”, 3: “c”, 4: “d”, 5: “e”}
