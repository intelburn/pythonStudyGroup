def findDups(raw=[]):
    processed={}
    for item in raw:
        if item in processed.keys():
            processed[item] += 1
        else:
            processed[item] = 1
    return processed

def printDups(dups={}):
    for dup in dups.keys():
        print("The name {0} occurreed {1} times".format(dup, dups[dup]))

names = ['bob', 'susan', 'bob', 'dan', 'susan']
nameDups = findDups(names)
printDups(nameDups)

print("\n")

students = ['rahul', 'susan', 'quesadilla', 'robert', 'cassandra', 'austin', 'sandra', 'quesadilla', 'rahul', 'austin']
studentDups = findDups(students)
printDups(studentDups)