def bimarySerach(arr, key, high, low):
    # There are Two formulae to calculate  Mid element
    # 1. (low+high)//2   example low =4 ang high =6 and answer is 4 but in our sub-array there is no index 4 present
    # so i have chose this below :  mid=low+(high-low)//2  low + (remaining element)//2  it solved my issue

    mid = low + (high - low) // 2

    if arr[mid] == key:
        return mid

    elif arr[mid] < key:
        new_low = mid + 1
        new_high = high
        return bimarySerach(arr, key, new_high, new_low)

    elif arr[mid] > key:
        new_low = low
        new_high = mid - 1
        return bimarySerach(arr, key, new_high, new_low)

    return -1


# collecting a Input from command line
arr = list(map(int, input().split()))
# Calculating The length of Input

# key to search
key = int(input("Enter A key To Search : "))
# Sort Array before passing to function
arr.sort()
# Calling a function which is used For searching  list for Element
pos = bimarySerach(arr, key, low=0, high=int(len(arr) - 1))

if pos != -1:
    print("element is Found at : ", pos)
