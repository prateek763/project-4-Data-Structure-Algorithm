def rearrange_digits(input_list, first_layer= False) -> list:
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]

    left = rearrange_digits(left)
    right = rearrange_digits(right)

    return merge(left, right, first_layer)


def merge(left, right, first_layer= False) -> list:
    merged = []
    left_index = 0
    right_index = 0

    if first_layer:  
        max_left = ''
        max_right = ''
        to_left = True


        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                if to_left:
                    max_left = str(right[right_index]) + max_left
                else:
                    max_right = str(right[right_index]) + max_right
                right_index += 1
            else:
                if to_left:
                    max_left = str(left[left_index]) + max_left
                else:
                    max_right = str(left[left_index]) + max_right
                left_index += 1

            to_left = not to_left  
        while left_index < len(left):   
            if to_left:
                max_left = str(left[left_index]) + max_left
            else:
                max_right = str(left[left_index]) + max_right

            left_index += 1
            to_left = not to_left

        while right_index < len(right):  
            if to_left:
                max_left = str(right[right_index]) + max_left
            else:
                max_right = str(right[right_index]) + max_right

            right_index += 1
            to_left = not to_left

        return [int(max_left), int(max_right)]

    else: 
        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                merged.append(right[right_index])
                right_index += 1
            else:
                merged.append(left[left_index])
                left_index += 1

        merged += left[left_index:]
        merged += right[right_index:]

        return merged



# Normal cases
list_num = [1, 2, 3, 4, 5]
print(rearrange_digits(input_list=list_num, first_layer=True))
# Output:-[531, 42]

list_num = [4, 6, 2, 5, 9, 8]
print(rearrange_digits(input_list=list_num, first_layer=True))
# Output:-[852, 964]

list_num = [1, 2, 3]
print(rearrange_digits(input_list=list_num, first_layer=True))
# Output:-[31, 2]

list_num = [1, 1, 1]
print(rearrange_digits(input_list=list_num, first_layer=True))
# Output:-[11, 1]

list_num = [1]
print(rearrange_digits(input_list=list_num, first_layer=True))
# Output:-[1]

list_num = []
print(rearrange_digits(input_list=list_num, first_layer=True))
# Output:-[]

