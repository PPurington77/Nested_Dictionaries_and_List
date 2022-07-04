# 1. change the value 10 in x to 15

x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
# print(x)

# 2. change the last name of the first student from jordan to bryant
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
# print(students[0]['last_name'])
# print(students)

# 3.change messi to andres
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory['soccer'])

# 4. change the value 20 in z to 30
z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30
# print(z)

# challenge #2

# 1. iterate through a list of dictionaries
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(some_list):
    i = 0
    while i < len(some_list):
        print(some_list[i])
        i += 1

# iterateDictionary(students)

# challenge #3
# get value from a list of dictionaries


def iterateDictionary2(key_name, some_list):
    x = 0
    while x < len(some_list):
        print(some_list[x][key_name])
        x += 1

# iterateDictionary2('last_name', students)

# challenge #4 iterate through a dictionary with list values


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    # print(some_dict) #accepts the function input test complete
    print(len(some_dict['locations']), "Locations")
    j = 0
    while j < len(some_dict['locations']):
        print(some_dict['locations'][j])
        j +=1
    print()
    print(len(some_dict['instructors']), "Instructors")
    g = 0
    while g < len(some_dict['instructors']):
        print(some_dict['instructors'][g])
        g +=1


printInfo(dojo)

