"""
def get_middle_three_chars(str1):
    print("Original String is ", str1)
    mi = int(len(str1)/2)
    res = str1[mi - 1:mi +2 ]
    print("Result is ", res)
get_middle_three_chars("JhonDipPeta")
get_middle_three_chars("JasonAy")



def append_middle(s1, s2):
    mi = int(len(s1) / 2)
    x = s1[:mi:] + s2 + s1[mi:]
    print("Result is ", x)


append_middle("Diyor", "Azim")


str1 = "PyNative"
lower, upper = [], []
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
result = ''.join(lower + upper)
print("Result is ", result)
"""

def string_balance_test(s1,s2):
    flag = True-
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag
print(string_balance_test("Yn","PyNative"))
print(string_balance_test("Ynf","PyNative"))

