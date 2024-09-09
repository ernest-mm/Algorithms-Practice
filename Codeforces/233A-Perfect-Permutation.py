# time limit per test2 seconds
# memory limit per test256 megabytes
# A permutation is a sequence of integers p1, p2, ..., pn, consisting of n distinct positive integers, each of them doesn't exceed n. Let's denote the i-th element of permutation p as pi. We'll call number n the size of permutation p1, p2, ..., pn.

# Nickolas adores permutations. He likes some permutations more than the others. He calls such permutations perfect. A perfect permutation is such permutation p that for any i (1 ≤ i ≤ n) (n is the permutation size) the following equations hold ppi = i and pi ≠ i. Nickolas asks you to print any perfect permutation of size n for the given n.

# Input
# A single line contains a single integer n (1 ≤ n ≤ 100) — the permutation size.

# Output
# If a perfect permutation of size n doesn't exist, print a single integer -1. Otherwise print n distinct integers from 1 to n, p1, p2, ..., pn — permutation p, that is perfect. Separate printed numbers by whitespaces.

# Examples
# Input
# 1
# Output
# -1
# Input
# 2
# Output
# 2 1 
# Input
# 4
# Output
# 2 1 4 3 

n = int(input())

if n % 2 != 0:
    print(-1)
else:
    # Building a dictionary of permutations
    permutations = dict()
    for i in range(1, n+1):
        permutations[i] = i

    # Becuse ppi = i, we need to statisfy pi != i. To do that we do a swap of two elements. It only works if n is even
    perfect = ''
    for i in permutations:
        if (2*i) <= n:
            if i == n/2:
                perfect += str(permutations[2*i]) + ' ' + str(permutations[(2*i) - 1])
            else:
                perfect += str(permutations[2*i]) + ' ' + str(permutations[(2*i) - 1]) + ' '
        
    print(perfect)