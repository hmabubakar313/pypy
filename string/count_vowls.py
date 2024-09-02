def count_vowels(s):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')  
    count = 0
    for i in range(len(s)):
        print(s[i])
        if s[i] in vowels:
            print("count", count)
            count += 1
    return count

# Test the function
print("Number of vowels:", count_vowels("BC"))  # Output should be 0
print("Number of vowels:", count_vowels("Hello World"))  # Output should be 3
