# username = "lakshmi raj"
# print(username.title())

# sentence = input('Enter sentence: ')
# new_sentence = sentence[::-1].replace(" ", "_")
# print(new_sentence)

# num = [10, 72, 13, 34, 6, 89, 20]
# num.sort()
# print(num)

# my_tuple = tuple(num)
# print(my_tuple)

# print(sum(my_tuple))

# set1 = {1, 3, 5, 7, 9, 0}
# set2 = {2, 4, 6, 8, 3, 1}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set1.symmetric_difference(set2))

# dict1 = {
#    's1' : {'name' : 'Lakshmi',
#    'age' : 23,
#    'grade' : 'A'},
#    's2' : {'name' : 'Sahva',
#    'age' : 21,
#    'grade' : 'A+'},
#    's3' : {'name' : 'Panchami',
#    'age' : 98,
#    'grade' : 'A'},
# }
# if dict1['age']>18 :
#    print(dict1['age'])

# number = int(input("Enter a number:"))
# if number >= 0:
#    if number == 0:
#       print('number equals to zero')
#    else:
#       print('positive number')
   
#    if number % 2  == 0:
#       print('even number')
#    else:
#       print('odd number')
      
#    if number % 5 == 0:
#       print('Divisible by 5')
#    else:
#       print('Not divisible by 5')
# else:
#    print('negative number')

# n = int(input('enter number:'))
# i = 1
# sum = 0 
# while i <= n:
#    sum = sum + i
#    i=i+1
# print(sum)


for i in range(1,21):
   if i > 10:
      if i % 2 == 0:
         print(f"{i} is an even number")


sentence = input('Enter a sentence:')
words = sentence.split()
print(words)
count = len(words)
print(count)
reversedwords = []
for i in words:
   reversed = i[::-1]
   reversedwords.append(reversed)
last_sent = " ".join(reversedwords)
print(last_sent)
   
   