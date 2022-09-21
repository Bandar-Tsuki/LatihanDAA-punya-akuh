a = 2
b = 3
c = 5
a, b, c = c, b, a

print(a,b,c)

list = [100,20,60,90,40,30,10]

def Bubblesort(list) :
    lastElementindex = len(list)-1
    for passNo in range(0,lastElementindex):
        for idx in range(lastElementindex) :
            if list [idx]>list[idx+1] :
                list[idx],list[idx+1]=list[idx+1],list[idx]
    return list

print(Bubblesort(list))

list = [50,20,70,30,10,120,90]

def bubble_sort(list):
    swap_count = 1
    pass_count = 0
    n = len(list)
    while swap_count > 0 and pass_count < n:
        swap_count = 1
        for i in range(0, n - pass_count - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swap_count += 1
        print(f'Pass {pass_count+ 1} : {list}')
        pass_count += 1
    return list

print(bubble_sort(list))

list = [90,20,50,10,80,30,60]

def insertion_sort(list):
    for i in range(1, len(list)):
        j = i - 1
        next = list[i]

        while (list[j] > next) and (j >= 0):
            list[j + 1] = list[j]
            j -= 1

        list[j + 1] = next
    
    return list

print(insertion_sort(list))

list = [9,2,1,5,7,3,8,4]

def selection_sort(list):
    for fill_slot in range(len(list) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if list[location] > list[max_index]:
                max_index = location
        list[fill_slot], list[max_index] = list[max_index], list[fill_slot]
    return list

print(selection_sort(list))

def linear_search(list, item):
    for elem in list:
        if elem == item:
            return True
    return False

list = [0,3,4,8,1,2,9]

print(linear_search(list, 1))

list = ['q','c','t','g','h','s','l','o','p','g','b']

print(linear_search(list, 'm'))

def binary_search(list, item):
    first = 0
    last = len(list) - 1
    
    while first <= last:
        mid = (first + last) // 2
        if list[mid] == item:
            return True
        else:
            if item < list[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return False

list = [10,50,30,90,20,80,60,70]
sorted_list = sorted(list)

print(binary_search(sorted_list, 10))
print(binary_search(sorted_list, 90))

def interpolation_search(arr, lo, hi, x):
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                    (x - arr[lo]))
        if arr[pos] == x:
            return True
        if arr[pos] < x:
            return interpolation_search(arr, pos + 1,
            hi, x)
        if arr[pos] > x:
            return interpolation_search(arr, lo,
            pos - 1, x)
    return False

list = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
n = len(list)
x = 18

print(interpolation_search(list, 0, n - 1, x))