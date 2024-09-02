def remove_duplicate(s):
    seen = set()         # Set to track seen characters
    result = []          # List to store characters without duplicates

    for c in s:
        if c not in seen:
            seen.add(c)
            result.append(c)
    return "".join(result)


# Testing the function
print(remove_duplicate("helllo"))  # Output: 'helo'
print(remove_duplicate("abcabc"))  # Output: 'abc'
