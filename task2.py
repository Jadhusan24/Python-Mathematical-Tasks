'''
inbuild func sort acending order -> storing in datas
current indexs (starts with 0)counts
we are modifying existing array so
in for loop we cant modify array
datas 2 5 6 8 6 5 4 
2
while loop runs until is their
'''

'''
idx+1 means we need the next index
Array wise 1 index number wise 2 index
2,7,8,10,17
'''

def filter_by_gap(arr, gap):
    sorted_arr = sorted(arr)
    idx = 0
    while sorted_arr:
        try:
            if (sorted_arr[idx+1] - sorted_arr[idx]) < gap:
                sorted_arr[idx+1] = sorted_arr[idx]
            idx += 1 
        except IndexError:
            break
    return sorted_arr

gap = int(input("Enter gap > "))
elem = int(input("Enter number of elements in list > "))

arr = []
while elem:
    arr.append(int(input("> ")))
    elem -= 1

result = filter_by_gap(arr, gap)
print(result)