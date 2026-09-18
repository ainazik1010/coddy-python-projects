def find_occurrences(text, pattern):
    found = False
    count = 0
    positions = []

    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            found = True
            count += 1
            positions.append(i)

    return (found, count, positions)


# Read input
text = input()
pattern = input()

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)
