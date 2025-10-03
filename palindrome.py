"""
🥋 Challenge: Palindrome Checker

📝 Description:
A palindrome is a word, phrase, number, or sequence of characters that reads the same backward as forward.
Examples: "radar", "level", "1221".

🎯 Task:
Write a Python function that receives a string and checks whether it is a palindrome.

📌 Requirements:
- Input: a string (can contain letters or numbers).
- Output: True if the input is a palindrome, False otherwise.
- Ignore spaces and capitalization (e.g., "Never odd or even" should be considered a palindrome).

✅ Example:
Input: "Radar"
Output: True

Input: "Python"
Output: False

⏱ Time Tracking:
- Date: 2025-10-04
- Time taken: 17m 42s
- Version: v1

💡 Observations:
- Focus on solving the challenge first.  
- A possible v2 could expand to handle phrases with punctuation (e.g., "A man, a plan, a canal, Panama").
"""

def invert_string(input: str) -> str:
    l = []
    for c in input:
        l.insert(0, c)
    
    invert_string = ""
    for el in l:
        invert_string += el

    return invert_string


def is_palindrome(input: str) -> bool:
    input = input.replace(" ", "").lower()    
    return input == invert_string(input)

print(is_palindrome("eye"))
print(is_palindrome("Never odd or even"))
print(is_palindrome("play"))
