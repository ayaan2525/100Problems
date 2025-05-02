# Return length of last word in a string
# Example:
# Input:  god is one
# Output: 3

inp_str = input("Enter string separated by space: ")

count = 0
for i in range(len(inp_str)):
    if inp_str[i] == " ":
        count = 0
    else:
        count += 1

print("Length of last word is:", count)


# Time: O(n)
# Space: O(1)
