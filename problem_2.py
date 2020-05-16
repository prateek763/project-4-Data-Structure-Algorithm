def rotated_array_search(input_list, number):
    return search(input_list,0,len(input_list)-1,number)

def search(arr,low,up,number):
         if low>up:
                  return -1
         else:
                  mid=(low+up)//2
                  if arr[mid]==number:
                           return mid
                  else:
                           left=search(arr,low,mid-1,number)
                           if left==-1:
                                    return search(arr,mid+1,up,number)
                           else:
                                    return left

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    print(rotated_array_search(input_list, number))
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Output:-0
#         Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# Output:-5
#         Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# Output:-2
#         Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# Output:-3
#         Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# Output:--1
#         Pass

test_function([[], -1])
# Output:--1
#         Pass
test_function([[1], 0])
# Output:--1
#         Pass
