# Python Program to Check If Two Strings are Anagram

str1 = "Race"
str2 = "Care"

# Convert both string to lowercase
str1 = str1.lower()
str2 = str2.lower()

# Check if length is same
if(len(str1) == len(str2)):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if(sorted_str1 == sorted_str2):
        print("Is anagram!")
    else:
        print("Not an anagram!")
else:
    print("Not an anagram")