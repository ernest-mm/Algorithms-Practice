"""
You are given a DNA sequence: a string consisting of characters A, C, G, and T. 
Your task is to find the longest repetition in the sequence. 
This is a maximum-length substring containing only one type of character.

Input
The only input line contains a string of n characters.
Output
Print one integer: the length of the longest repetition.
Constraints

1 <= n <= 10^6

Example
Input:
ATTCGGGA

Output:
3
"""
def repetitions():
    seq = input()
    seq = ' ' + seq
    max = 0
    temp_max = 0
    start = 1
    stop = 1

    for i in range(1, len(seq)):
        if i > start:
            stop = i-1

        if seq[i] != seq[start]:
            temp_max = (stop - start) + 1
            if i < len(seq)-1:
                start = i
                stop = i
        elif i == len(seq)-1:
            temp_max = (i - start) + 1

        if temp_max > max:
            max = temp_max
    
    print(max)

repetitions() 
