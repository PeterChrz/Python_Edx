s = 'hiyou'
print()

lst = []
for i in range(len(s)):
    if not i % 2:
        lst.append(i)
    print(lst)
print("n so we filtered for evenness & stored results \n")


newstring = ""
for c in s:
    if c in 'hio':
        newstring += c
    print(newstring, end = ', ')
print("\n we filtered for inclusion & store the in crowd\n")
