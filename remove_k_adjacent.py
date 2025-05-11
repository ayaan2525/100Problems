# Function to remove k adjacent duplicate characters from a string
def remove_k_adjacent(s, k):
    stack = []  # Stack to keep track of characters and their counts

    for ch in s:
        if stack and stack[-1][0] == ch:
            stack[-1][1] += 1  # Increase the count if same character
            if stack[-1][1] == k:
                stack.pop()  # Remove the group if count reaches k
        else:
            stack.append([ch, 1])  # Add new character with count 1

    result = ''
    for char, count in stack:
        result += char * count  # Rebuild the final string
    return result

# Main
def main():
    input_str = input("Enter input string: ")
    k = int(input("Enter k: "))

    if k == 1:
        print("")
        return

    if k > len(input_str):
        print("k cannot be larger than string length.")
        return

    output = remove_k_adjacent(input_str, k)
    print("Output:", output)

# Call the main
main()