def first_non_repeating_char(s):
    char = {}
    # Loop through the string to count occurrences
    for c in s:
        if c in char:
            char[c] += 1  # Increment count if char is already in the dictionary
        else:
            char[c] = 1 
    non_repeating = [c for c in s if char[c] == 1]
    
    return non_repeating if non_repeating else None  # Return None if no non-repeating chars found


print(first_non_repeating_char("aabbc"))
print(first_non_repeating_char("abc"))