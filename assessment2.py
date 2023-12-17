                  # PYTHON PROGRAMS

# Question 1 :
# Write a fuction that takes a tuple as input and returns a new tuple with the elements in the reverse order.
def reverse_tuple(collection):
    return collection[::-1]


a = (1, 2, 3, 4, 5)
print(reverse_tuple(a))

#################################################################################################################

# Question 2 :
# Write a function that takes the tuple as an input and returns a new tuple with all the duplicate elements removed
def remove_duplicates_from_tuple(collection):
    res = []
    for i in collection:
        if i not in res:
            res.append(i)
    return tuple(res)


a = (1,2,3,4,5,1,2,3)
print(remove_duplicates_from_tuple(a))

#################################################################################################################

# Question 3:
# Given a string the task is to check if the string is symmetrical and palindrome or not.
# A string is said to be symmetrical if both the halves of the string are the same and
# a string is said to be a palindrome string if one half of the string is the reverse of the other half
# or if a string appears same when read forward or backward.
def symmetrical_and_palindrome(string):
    if len(string) % 2 == 0:
        half = len(string)//2
        first = string[0:half:]
        last = string[half::]
        if first == last:
            print("The entered string is symmetrical ")
        else:
            print("The entered string is not symmetrical ")

        if string == string[::-1]:
            print("The entered string is palindrome")
        else:
            print("The entered string is not palindrome")


a = ["khokho","amaama"]
for item in a:
    symmetrical_and_palindrome(item)

#################################################################################################################

# Question 4:
# Given a string. The task is to print all words with even length in the given string.
def even_words(string):
    words = string.split()
    li = []
    for item in words:
        if len(item)%2 == 0:
            li.append(item)
    res = " ".join(li)
    return res


a = "This is a python language"
print(even_words(a))

#################################################################################################################

# Question 5:
# Sort the dictionary by keys and values in Python. Here, iterkeys() returns an iterator over the dictionary’s keys.
def sort_key_value(dictionary):
    res = {}
    keys = sorted(dictionary.keys())
    values = sorted([int(i) for i in dictionary.values()])
    for key, value in zip(keys,values):
        if key not in res:
            res[key] = str(value)
    return res


d = {2: '56', 1: '2', 4: '12', 5: '24', 6: '18', 3: '323'}
print(sort_key_value(d))


#################################################################################################################
# Question 6:
# Write a function that takes a list of numbers as input and returns the sum of all the numbers in the list.
def sum_of_list(list1):
    return sum(list1)


li = [1, 2, 3, 4, 5]
print(sum_of_list(li))

#################################################################################################################
# Question 7:
# Write a function that takes a string as input and returns the reverse of the string.
def reversed_string(collection):
    return collection[::-1]


a = "Hello, world!"
print(reversed_string(a))

#################################################################################################################
# Question 8:
# How to get the maximum and minimum element in a set in Python, using the built-in functions of Python.
a = (8, 16, 24, 1, 25, 3, 10, 65, 55)
print(max(a))
print(min(a))

#################################################################################################################
# Question 9 :
# Given two lists a, b.
# Check if two lists have at least one element common in them.
def element_check(a,b):
    for i in a:
        if i in b:
            return True
    return False


a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(element_check(a, b))

#################################################################################################################
# Question 10:
# Given two strings (of lowercase letters), a pattern and a string. The task is to sort string according
# to the order defined by pattern and return the reverse of it. It may be assumed that pattern has all characters
# of the string and all characters in pattern appear only once.
def pattern(string,substring):
    res = ""
    for i in string:
        for j in substring:
            if i==j:
                res = i+res
    return res


st = "asbcklfdmegnot"
sub = "eksge"
print(pattern(st, sub))

st = "mgewqnasibkldjxruohypzcftv"
su = "niocgd"
print(pattern(st, su))

#################################################################################################################
# Question 11:
#Make a class FLashcard.
#Take the word and its meaning as input from the user.
#Create a class named flashcard, use the __init__() function to assign values for Word and Meaning.
#Now we use the __str__() function to return a string that contains the word and meaning.
# Store the returned strings in a list named flash.
class Flashcard:

    def __init__(self, word, meaning):
            self.word = word
            self.meaning = meaning
            self.flashcards = []

    def __str__(self):
            wordmean = f"Word: {self.word}\nMeaning: {self.meaning}"
            self.flashcards.append(wordmean)


word = input("Enter a word: ")
meaning = input(f"Enter the meaning of '{word}': ")

flash = Flashcard(word, meaning)
print(flash.flashcards)


string = "chandu veerapuram"
res = {}
for i in string:
    if i not in res:
        res[i] = 1
    else:
        res[i] += 1

y = sorted(res.items(), key=lambda x: x[1])
print(y)
print(dict(y))


def prime(start,end):
        for num in range(start, end):
            if num > 1:
                for i in range(2,num-1):
                    if num%i == 0:
                        break
                else:
                    print(num)

prime(10,20)


