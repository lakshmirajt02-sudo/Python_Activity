# Level 1  - Basic
# ----------------
# numbers = [10, 20, 30, 40, 50]
# print(numbers[0])
# print(numbers[-1])
# print(numbers[2])
# print(numbers[0:3])
# print(numbers[-2:])
# print(numbers[::-1])
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# Level 2  - List methods
# -----------------------
# fruits = ['Apple', 'Banana', 'Orange']
# fruits.append('Mango')
# print(fruits)

# fruits.insert(1,input('Enter the fruit to be inserted: '))
# print(fruits)

# fruits.remove('Banana')
# print(fruits)

# fruits.pop()
# print(fruits)

# fruits.pop(0)
# print(fruits)

# fruits.clear()
# print(fruits)

# index_value = fruits.index('Orange')
# print(index_value)

# fruits = ['Apple', 'Banana', 'Apple', 'Orange']
# print(fruits.count('Apple'))

# num = [45, 10, 78, 22, 5]
# num.sort()
# print(num)
# num.sort(reverse = True)
# print(num)

# Level 3  - Slicing 
# ------------------
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# print(numbers[1::2])
# print(numbers[2:6])
# print(numbers[2::3])
# print(numbers[1:])
# print(numbers[:-1])

# Level 4  - Operators
# --------------------
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# new_list = list1 + list2
# print(new_list)
# print(len(new_list))

# colors = ['Red', 'Blue']
# print(colors * 3)

# languages = ['Java', 'Python', 'C++']
# print('Python' in languages)
# print('PHP' not in languages)

# Level 5 - Logical Thinking 
# --------------------------
# num = [15, 2, 3, 4, 50]
# new_num = num.copy()
# reversed = new_num.reverse()
# print(new_num)

# print(max(num) - min(num))

# numbers = [20, 30, 40, 50]
# average = sum(numbers) / len(numbers)
# print(average)

# num = [10, 20, 30, 40, 50]
# # new_num = min(num) , max(num)   or
# new_num = num[0::4]
# print(list(new_num))

# number = [1, 2, 3]
# dup_num = number * 2
# print(dup_num)

# dup_num[5] = 100
# print(dup_num)
# dup_num[0] = 0
# print(dup_num)

# new_number = dup_num.copy()
# print(new_number)

# new_number.sort()
# print(new_number)
# print(new_number[-2])
# print(new_number[1])

# Challenge questions
# -------------------
# numbers = [10, 20, 30, 40, 50]
# print(numbers[2])

# temp = numbers[0]
# numbers[0] = numbers[4]
# numbers[4] = temp
# print(numbers)

# new_list = list(numbers[:3])
# print(new_list)

# numbers.remove(30)
# print(numbers)
# l1 = [10, 20]
# l2 = [30, 50]
# l3 = [6, 7]
# merged = l1+ l2 + l3
# print(merged)

languages = ['python', 'java', 'python', 'c', 'python']
print(languages.count('python'))

first_half  = languages[:3]
print(first_half)

second_half  = languages[3:]
print(second_half)

print(min(languages))
print(max(languages))

tuple = tuple(languages)
print(tuple)









