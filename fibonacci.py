"""
🥋 Challenge: Fibonacci Sequence

📝 Description:
The Fibonacci sequence starts with 0 and 1. Each new number in the sequence is the sum of the two preceding ones.
Example: 0, 1, 1, 2, 3, 5, 8, ...

🎯 Task:
Write a Python function that receives an integer `n` and returns the Fibonacci sequence up to the n-th element.

📌 Requirements:
- Input: an integer n (n ≥ 1).
- Output: a list containing the Fibonacci sequence with n elements.
- The function should work for any reasonable value of n (ex: up to 50).

✅ Example:
Input: n = 7
Output: [0, 1, 1, 2, 3, 5, 8]

⏱ Time Tracking:
- Date: 2025-09-16
- Time taken: 20m 36s
- Version: v1
"""

def seq_fibonacci(n: int):
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return seq_fibonacci(n-1) + seq_fibonacci(n-2)

def get_fibonacci_list(n: int):
    list_numbers = []
    for i in range(n):
        number = seq_fibonacci(i+1)
        list_numbers.append(number)
    
    return list_numbers

print(get_fibonacci_list(10))
