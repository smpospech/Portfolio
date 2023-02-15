import time

def binSearch(arr, start, finish, goal):
    if (start > finish):
        return
    middle = (start + finish) // 2

    if (goal == arr[middle]):
        return middle

    if (goal < arr[middle]):
        return binSearch(arr, start, (middle - 1), goal)
    else:
        return binSearch(arr, (middle + 1), finish, goal)

def battery(len, start=time.perf_counter()):
    for _ in range(20000):
        binSearch(list(range(len)), 0, len - 1, len)
    return time.perf_counter() - start

clock = [(len, battery(len)) for len in [100, 400, 1600, 6400, 25600, 102400, 409600, 1638400]]
[print(f"{map[0]}\t\t{map[1]} seconds") for map in clock]