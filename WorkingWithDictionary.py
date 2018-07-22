import operator


d = {1: 'a', 3: 'c', 4: 'd', 2: 'b', 0: 'x'}

print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)
print('Dictionary in descending order by value : ',sorted_d)



dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')

is_key_present(5)
is_key_present(9)


d = {'x': 10, 'y': 20, 'z': 30}
for dict_key, dict_value in d.items():
    print(dict_key,'->',dict_value)

for key in sorted(d):
    print(key, '=>', d[key])

print(list(d.items()))
print(list(d.keys()))
print(list(d.values()))

def squaredict(n):
    d = dict()

    for x in range(1, n + 1):
        d[x] = x * x

    print(d)

squaredict(15)

#Write a Python script to merge two Python dictionaries
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)


myDict = {'d':1,'c':2,'b':3,'a':4}
print("This is my dictionary: ", myDict)


sortbyvalues = sorted(myDict.items(),key= lambda t: t[1])
print("This is my dictionary sorted by values: ", sortbyvalues)
sortbykeys = sorted(myDict.items(),key= lambda t: t[0])
print("This is my dictionary sorted by keys: ", sortbykeys)

if 'a' in myDict:
    del myDict['a']
print("This is my dictionary without the a key: ",myDict)

if 'a' not in myDict:
    myDict['a'] = 4
print("This is my dictionary updated back with a: ", myDict)


multiplicator = 2
for x in myDict:
    result = multiplicator * myDict[x]
    print("The value of",myDict[x]," is multoplied by", multiplicator, " which equates to: ", result)


print("The sum of the values in myDict is: ",sum(myDict.values()))


x = 'a' #change this
print("Looking for key", x,"in myDict and the matched value is:",myDict.get(x,'The key is not found in myDict'))

newmyDict = myDict.copy()
newmyDict['a'] = 99
print("Old dict:",myDict)
print("New dict:",newmyDict)

myDict2 = {'x':5,'y':6,'z':7,'v':8}
myDict.update(myDict2)
print("My second dict is: ", myDict2)
print("My first updated dict is: ", myDict)


myList1 = ['d','c','b','a']
myList2 = [1, 2, 3,4]
mynewList = zip(myList1,myList2)
myDict = dict(mynewList)
print("My dict made from two lists: ",myDict)

print("The minimum value from my dict is: ", min(zip(myDict.values(),myDict.keys())))
print("The maximum value from my dict is: ", max(zip(myDict.values(),myDict.keys())))

print("Check if the two dictionaries are equal: ", operator.eq(myDict,myDict2))