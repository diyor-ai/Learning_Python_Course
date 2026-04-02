# Remove empty prases
"""

str_list = ["Emma", "John", "Kelly",None, "Eric",""]
new_list= [s for s in str_list if s ]

print(new_list)

import string

str1 = "/*Jon is @developer & musician"

# Remove punctuation
no_punct = ""
for char in str1:
    if char not in string.punctuation:
        no_punct += char

print(no_punct)


str1 = " I am 25 years and 10 month old"
result = ''.join([char for char in str1 if char.isdigit()])
print(result)
import string

str1 = "/*Jon is @developer & musician!!"

# Replace each punctuation symbol with '#'
for char in string.punctuation:
    str1 = str1.replace(char, "#")

print(str1)

"""


def is_palindrome(s):
    processed_s = ""
    for char in s:
        if char.isalnum():  # Keep only letters and numbers
            processed_s += char.lower()  # Convert to lowercase

    # Check if the cleaned string equals its reverse
    return processed_s == processed_s[::-1]


# Test cases
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False