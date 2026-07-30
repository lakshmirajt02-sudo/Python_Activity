# BASIC LEVEL 
# numbers divisible by 3 
newlist=[]
for i in range(1,51):
   if i % 3 == 0:
      newlist.append(i)
print(newlist)

# Right-angle triangle pattern
for i in range(6):
   for j in range(i):
      print("*", end=" ")
   print()
   
# reverse triangle pattern 
for a in range(6):
   for b in range(5,1):
      print("*", end= " ")
   print()
   

