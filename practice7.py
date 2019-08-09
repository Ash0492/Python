a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#c = []
#for i in a:
 #   if i%2==0:
  #      c.append(i)
   #     print(c)

   #Printing above code in one line using list comprehension

c = [i for i in a if i%2==0]
print (c)

    
