"""
You are given all numbers between 1,2,...,n except one. Your task is to find the missing number.

Input
The first input line contains an integer n.
The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).

Output
Print the missing number.
Constraints

2 <= n <= 2*10^5

Example
Input:
5
2 3 1 5

Output:
4
"""
def missing_number():
    n = int(input())
    sequence = set([int(x) for x in input().split()])
    
    if n == 2:
        missing_num = 1
    else:
        missing_num = None

    for num in sequence:
        if (num < n) and (num+1 not in sequence):
            missing_num = num+1

    print(missing_num)

missing_number()
