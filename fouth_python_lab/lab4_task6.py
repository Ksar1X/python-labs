from headers import *

def split_group(students, group_size):
    return list(itertools.combinations(students, group_size))

student = ["s1", "s2", "s3", "s4"]
result = split_group(student, 3)
print(result)