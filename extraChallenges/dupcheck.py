def findDups(raw=[]):
    processed={}
    for item in raw:
        if item in processed.keys():
            processed[item] += 1
        else:
            processed[item] = 1
    return processed

names = ['bob', 'susan', 'bob', 'dan', 'susan']
nameDups = findDups(names)
for name in nameDups.keys():
    print("The name {0} occurreed {1} times".format(name, nameDups[name]))

print()
print()

students = ['rahul', 'susan', 'quesadilla', 'robert', 'cassandra', 'austin', 'sandra', 'quesadilla', 'rahul', 'austin']
studentDups = findDups(students)
for student in studentDups.keys():
    print("The name {0} occurreed {1} times".format(student, studentDups[student]))