# BASIC LEVEL 
# numbers divisible by 3 
newlist=[]
for i in range(1,51):
   if i % 3 == 0:
      newlist.append(i)
print(newlist)

# Right-angle triangle pattern
# for i in range(6):
#    for j in range(i):
#       print("*", end=" ")
#    print()
   
# reverse triangle pattern 
for a in range(5,0,-1):
   for b in range(a):
      print("*", end= " ")
   print()
   
#  Use of break
for i in range(1,11):
   print(i)
   if i == 5:
      break
     
#  Use of continue
for j in range(1,6):
   if j == 3:
      continue
   print(j)

