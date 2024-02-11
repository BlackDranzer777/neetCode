'''

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

'''

Input = ["eat","tea","tan","ate","nat","bat"]


dictionary = {}

print(ord('b') - ord('a'))

for word in Input:
    word_count = [0]*26
    for character in word:
        word_count[ord(character) - ord('a')]+=1
    if tuple(word_count) in dictionary:
        dictionary[tuple(word_count)].append(word)
    else:
        dictionary[tuple(word_count)] = [word]

print(dictionary.values())
