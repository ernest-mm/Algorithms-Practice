def num_moves():
    n = int(input())
    array = [int(x) for x in input().split()]

    result = 0

    for i in range(n):
        if (i<n-1) and (array[i] > array[i+1]):
            delta = array[i] - array[i+1]
            result += delta
            array[i+1] += delta
    print(result)

num_moves()
