"""
Reverse the string.
i/p: hello
o/p: olleh
"""
input_str = input("Enter string: ")

# def reverse_str(input_str):
    
#     stack = list(input_str)
#     reverse_chars = []
#     while stack:
#         reverse_chars.append(stack.pop())
#     return ''.join(reverse_chars)


# Time complexity: O(n)
# Space complexity: O(n)


def reverse_in_place(input_str):

    reverse_lst = list(input_str)
    left, right = 0, len(input_str)-1

    while left < right:
        reverse_lst[left], reverse_lst[right] = reverse_lst[right], reverse_lst[left]
        left += 1
        right -= 1
    return ''.join(reverse_lst)

print(reverse_in_place(input_str))

# Time complexity: O(n)
# Space complexity: O(n)