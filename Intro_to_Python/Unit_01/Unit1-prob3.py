#!/usr/bin/env python3


s = 'hiyou'
print()

#lets save index numbers.
lst = []
for i in range(len(s)):
    if not i % 2:
        lst.append(i)
    print(lst, end = ', ')
print("n so we filtered for evenness & stored results \n")


# Save characters in a string
newstring = ""
for c in s:
    if c in 'hio':
        newstring += c
    print(newstring, end = ', ')
print("\n we filtered for inclusion & store the in crowd\n")


# Save characters in a list then join it
lst = []
for c in s:
    if c in 'yu':
        lst.append(c)
    print(lst, end = ', ')
strung_list = "".join.list
print("\n Strung_list is ", strung_list)