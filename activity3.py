# list 
# movies = ['interstellar', 'tenant', 'avatar', 'gladiator', 'inception']
# print(movies[len(movies) // 2])

# movies.append('lucy')
# print(movies)

# movies.sort()
# print(movies)

# new_tuple = tuple(movies)
# print(new_tuple)

# first = new_tuple[0]
# last = new_tuple[-1]
# print(first , last)

# new_tuple[0] = 'wolverine'

# set & dict 
# set1 = {1, 3, 5, 7, 6}
# set2 = {2, 4, 6, 8, 3}
# new_set = set1.union(set2)
# new_set = set1.intersection(set2)
# new_set = set1.difference(set2)
# new_set = set1.symmetric_difference(set2)
# print(new_set)

# set1.add(10)
# print(set1)

# set1.remove(10)
# print(set1)

student_dict = {
   'name' : 'Lakshmi',
   'age' : 23,
   'grade' : 'A'
}
print(student_dict.keys())
print(student_dict.values())
print(student_dict.items())

student_dict['grade'] = 'A+'
student_dict.pop('age')
print(student_dict)




