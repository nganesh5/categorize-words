# Categorize words into dictionary based on key as the first letter

import random

from pkg_resources import working_set
from englishwords import words

def categorizewords(letter, letter_count):
    categorized_words = {}
    full_list = []
    word_list = []
    word_listall = []

    for word in words:
        firstletter = word[0]
        categorized_words.setdefault(firstletter, []).append(word)
    
    full_list = categorized_words[letter]
    
    for word in full_list:
        if len(word) == letter_count:
            word_list.append(word)
        else:
            word_listall.append(word)    
    
    for i in range(len(word_list)):
        print(word_list[i])
        
userletter = input("Enter letter to list words starting from: ")
count = int(input("What letter word would you like to see? (3-6) or (all - 0): "))
    
categorizewords(userletter, count)
