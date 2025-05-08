"""
Find the longest common prefix:
i/p: abc ab a
o/p: a
"""

input_str = input("Enter strings: ").split()

if not input_str:
    print("")
else:
    common_prefix = input_str[0]

    for seq in input_str[1:]:
        j = 0
        prefix = ""
        for ch in seq:
            if j < len(common_prefix) and ch == common_prefix[j]:
                prefix += ch
                j += 1
            else:
                break
        common_prefix = prefix
        if not common_prefix:
            break

    print(common_prefix)

# Time complexity: O(S), s is the total no of characters in all strings combined.
# We may need to check every character once in worst case, e.g. (dog dog dog)

# Space complexity: O(1)