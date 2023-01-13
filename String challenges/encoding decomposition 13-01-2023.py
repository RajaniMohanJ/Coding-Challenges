"""Coding Challenge
Given a encoded instruction in the form S1[k1]S2[S3[k2]]k3, such that S1,S2,S3 are positive integers and
k1, k2, k3 are alphabets. Create a function such that it decomposes the encoded instruction in a way
that each S is repeated its preceding k number of time and prints it. For eg. 3[A]2[3[B]]C would be
decomposed by the function into AAABBBBBBC. If any of the k values is 1 then instead of 1[A] it is given
as just A. """

def decomposition(s):
    list_ks = []

    for i in range(len(s)):
        if s[i].isalnum():
            list_ks.append(s[i])

    a = ''.join(list_ks)

    list_ks1 = []

    for j in range(len(a)):
        if j == 0 and a[j].isnumeric():
            pass
        elif j == 0 and a[j].isalpha():
            list_ks1.append(a[j])
        elif a[j].isnumeric():
            pass
        elif a[j].isnumeric() and a[j - 1].isnumeric():
            pass
        elif a[j].isalpha() and a[j - 1].isnumeric() and a[j - 2].isnumeric():
            list_ks1.append(''.join(int(a[j - 2]) * int(a[j - 1]) * a[j]))
        elif a[j].isalpha() and a[j - 1].isnumeric():
            list_ks1.append(''.join(int(a[j - 1]) * a[j]))
        elif a[j].isalpha():
            list_ks1.append(a[j])

    b = ''.join(list_ks1)

    return print(b)

text_0 = '3[A]2[3[B]]C'
text_1 = 'A2[3[B]]C'
text_2 = '3A3[B]C'
text_3 = 'ABC'

decomposition(text_0)
decomposition(text_1)
decomposition(text_2)
decomposition(text_3)