    n = int(input())
    arr = list(map(int, input().split()))  # convert to list
    arr = list(set(arr))  # removes duplicates
    arr.sort()            # sort ascending
    print(arr[-2]) 
