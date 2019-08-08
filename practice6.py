word = str(input('Enter a word:'))
rvs = word[::-1]
print(rvs)
if word == rvs:
    print('This is a pallindrome')
else:
    print('This is not a pallindrome')