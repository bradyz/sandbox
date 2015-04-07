# Write a method to decide if two strings are anagrams or not.

a = "asdf"
b = "adsf"

# O(nlogn) time, O(1) space
if sorted(a) == sorted(b):
    print("Anagram")

# O(n) time, O(n) space for map method
from collections import Counter

if Counter(a) == Counter(b):
    print("Anagram")
