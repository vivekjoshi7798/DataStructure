def desSort(a):
    l = len(a)

    for i in range(0, l):
        for j in range(i + 1, l):
            if a[j] > a[i]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    print('', a)

# //len function is giving value more than actual indexes but range function reducing 1 from given high indexed that
# why we are not reduced it
def AscSort(a):
    l = len(a)

    for i in range(0, l):
        for j in range(i + 1, l):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp

    print('', a)


arr = list(map(int, input("Enter A Data ").split()))

print('-----------descending  Order -------------')
desSort(arr)

print('-----------Ascending Order ---------------')
AscSort(arr)
