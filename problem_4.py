def sort_012(input_list):     
    i0=0
    i2=len(input_list)-1
    k=0
    while k<=i2:
        if input_list[k]==0:
            input_list[k]=input_list[i0]
            input_list[i0]=0
            i0+=1
            k=k+1
        elif input_list[k]==2:
            input_list[k]=input_list[i2]
            input_list[i2]=2
            i2-=1
        else:
            k=k+1
    return input_list
         
def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# Output:-[0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
#         Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# Output:-[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
#         Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# Output:-[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
#         Pass

test_function([0, 1, 1, 0, 1])
# Output:-[0, 0, 1, 1, 1]
#         Pass
test_function([0, 0, 0])
# Output:-[0, 0, 0]
#         Pass
test_function([])
# Output:-[]
#         Pass
