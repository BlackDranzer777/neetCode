'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''

s = 'anagram'
t = 'nagaram'

my_dictionary = dict()
for letter in s:
    if(letter in my_dictionary):
        my_dictionary[letter]+=1
    else:
        my_dictionary[letter] = 1
print(my_dictionary)


dictionary_t = dict()
for letter in t:
    if(letter in dictionary_t):
        dictionary_t[letter]+=1
    else:
        dictionary_t[letter] = 1
print(dictionary_t)

def isAnagram(dictionary_t, my_dictionary):
    if(dictionary_t.items() == my_dictionary.items()):
        return True
    else:
        return False

print(isAnagram(dictionary_t, my_dictionary))