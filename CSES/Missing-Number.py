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
