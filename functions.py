x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)
students[0]['last_name'] = 'Bryant'
print(students)
sports_directory['soccer'][0] = "Andres"
print(sports_directory)
z[0]['y'] = 30
print(z)

print('-------------------------- Problem 2 -----------------')
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for i in some_list:
        print(i)
print(iterateDictionary(students))
    
print(students[0]['first_name'])
print('-------------------------- Problem 3 -----------------')


def iterateDictionary2( key_name,some_list):
    
    for i in some_list:
       
        print(i[key_name])
iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)
print('-------------------------- Problem 4 -----------------')

def printInfo(some_dict):
    for i in some_dict:
        print(len(some_dict[i]),i)
        for j in some_dict[i]:
            print(j)
printInfo(sports_directory)