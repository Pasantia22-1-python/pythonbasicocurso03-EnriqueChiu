import random

def binary_search(data, target, init, end):
    if init > end:
        return False
    
    mid = (init + end) // 2

    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, init, mid-1)
    else:
        return binary_search(data, target, mid+1, end)

def binary_search_loop(data, target):
    mid = len(data)//2
    init = 0
    end = len(data)-1

    while True:
        if init > end:
            return False
        elif target == data[mid]:
            return True
        elif target < data[mid]:
            end = mid-1
            mid = (init+end)//2
        else:
            init = mid + 1
            mid = (init+end)//2

if __name__ == '__main__':
    data = [random.randint(0,100) for i in range(10)]

    data.sort()
    print(data)

    target =int(input("What number would you like to find? "))
    found = binary_search(data, target, 0, len(data)-1)
    found_loop = binary_search_loop(data, target)

    print("recursividad")
    print(found)
    print("sin recursividad")
    print(found_loop)

