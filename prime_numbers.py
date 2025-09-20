"""
🥋 Challenge: Prime Numbers

📝 Description:
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
The first prime numbers are: 2, 3, 5, 7, 11, 13, ...

🎯 Task:
Write a Python function that receives an integer `n` and returns a list with the first `n` prime numbers.

📌 Requirements:
- Input: an integer n (n ≥ 1).
- Output: a list containing the first `n` prime numbers.
- The function should work for any reasonable value of n (ex: up to 1000).

✅ Example:
Input: n = 10
Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

⏱ Time Tracking:
- Date: 2025-09-21
- Time taken: -
- Version: v1
"""

def is_prime_number(num: int):
    max_divisors = 2
    for i in range(num):
        divisor = i + 1
        if(num % divisor == 0):
            max_divisors -= 1
        if max_divisors < 0:
            break
  
    return max_divisors == 0

while(True):
    number = input("enter a number or x to exit: ")
    if number.lower() == 'x':
        break

    number = int(number)
    prime_numbers_list = []
    for i in range(number):
        seq_number = 1
        while(len(prime_numbers_list) < number):
            if(is_prime_number(seq_number)):
                prime_numbers_list.append(seq_number)
            seq_number += 1
    
    print(prime_numbers_list)
