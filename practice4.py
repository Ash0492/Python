num = int(input('Enter a number of your choice:'))
y = range(1,100)
for i in y:
    if num%i == 0:
        print(i)

#############above code in one line

print([i for i in y if num%i==0])