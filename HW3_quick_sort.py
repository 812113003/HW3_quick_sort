data = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]

def quicksort(array, left, right):
    if left < right:
        print(data)
        #print(array[right])
        partition_pos = partition(array, left, right)
        quicksort(array, left, partition_pos - 1) #(data,0,4)(1,4)(1,3)
        quicksort(array, partition_pos + 1, right) #(data,6,9)(6,8)

def partition(array, left, right): #(data,0,9)
    i = left #0 =33
    j = right - 1 #8 =25
    pivot = array[right] #9 =41
    while i < j:
        while i < right and array[i] < pivot: #1 =67 ,4 =54
            i += 1
        while j > left and array[j] > pivot: #8 =25, 6 =3
            j -= 1
        if i < j: #1 =25,8 =67, 4 =3,6 =54,
            array[i], array[j] = array[j], array[i]
    if array[i] > pivot: #5
        array[i], array[right] = array[right], array[i]
    return i #33,25,8,13,3,41,54,84,67,119->i = 5

quicksort(data, 0, len(data) - 1)
print(data)
