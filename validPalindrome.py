def is_palindrome_range(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

def can_be_palindrome(s):
    start, end = 0, len(s) - 1

    while start < end:
        if s[start] != s[end]:
            # Try deleting one character: either from start or end
            return is_palindrome_range(s, start + 1, end) or is_palindrome_range(s, start, end - 1)
        start += 1
        end -= 1
    return True

# Run Input and Output
input_str = input("Enter string: ")
if can_be_palindrome(input_str):
    print("Palindrome")
else:
    print("Not palindrome")
