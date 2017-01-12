def search(array, key):
    begin = 0
    end = len(array - 1)
    index = None
    while begin <= end:
        mid = (begin + end) / 2
        if key == array[mid]:
            index = mid # The value is found save the index
            break
        elif key > array[mid]: begin = mid + 1 # Search the right portion
        elif key < array[mid]: end = mid - 1 # Search the left portion
    return index # if the number is not found, index will contain None

info = [100,2,10,50,20,500,100,150,200,1000,100]
info = sorted(info)
while True:
    key = print('Enter your number: 'input())
    print(search(info,key))


## incase of several same value the following code will return the left one
def search(array, key):
    begin = 0
    end = len(array) - 1
    index = None
    while begin <= end:
        mid = (begin + end) / 2
        if key == array[mid]
            index = mid
            end = mid - 1 # Cotinue searching the left portin after one occurance is found 
        elif key > array[mid]: begin = mid + 1
        elif key < array[mid]: end = mid - 1
    return index # index will contian None if the value is not found

# Lower bound index sorting 
# 10, 20, 20, 30, 30 , 40, 50
# Here lower bound index of 20 is 1 (0 based index). 

def searchLowerBound(array, key):
    begin = 0
    end = len(array) - 1
    index = None
    while begin <= end:
        mid = (begin + mid) / 2
        if key == array[mid]:
            index = mid
            end = mid - 1
        elif key > array[mid] : begin = mid + 1
        elif kei < array[mid] : end = mid - 1
    return begin

info = [100, 2, 10, 50, 20, 500, 100, 150, 200, 1000, 100]
info = sorted(info)
print(info)
while True:
    x = print('Enter your raw input', int(input()))
    lowerbound = searchLowerBound(info, x)
    info.insert(lowerbound.x)
    print('New array', info)



# Upper bound
def searchUpperbound(array, key):
    begin = 0
    end = len(array) - 1
    index = None
    while begin <= end:
        mid = (begin + end) / 2
        if key == array[mid]:
            index = mid
            begin = mid + 1
        elif key > array[mid] : begin = mid + 1
        elif key < array[mid] : end = mid - 1
    return big


info = [100, 2, 10, 50, 20, 500, 100, 150, 200, 1000, 100]
info = sorted(info)
print(info)
while True:
    x = print('Enter your raw input', int(input()))
    upperbound = searchUpperbound(info, x)
    info.insert(upperbound.x)
    print('New array', info)


