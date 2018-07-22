Alist = ['aa','cc','bb','dd','ee']
print("My original list:", Alist)

Alist.append('ff')
print("My appended list: ", Alist)
Alist.pop(4)
print("My popped list: ", Alist)
Alist.reverse()
print("Reversed list:", Alist)
Alist.sort()
print("Sorted list", Alist)

Blist = [1,2,3,4,5,6,7,8,9]
ABlist = []
ABlist.append(Alist)
ABlist.append(Blist)
print("Appended ABlist: ", ABlist)

Alist.append('gg')
print("Appended Alist: ", Alist)
Alist.insert(4,'ee')
print("Insert ee into Alist: ", Alist)
Blist.remove(Blist[len(Blist)-1])
print("Removed item position 9 from the Blist: ", Blist)

Alist.extend(['hh','jj','gg'])
Blist.extend([10,11,12])
print("Extended Blist: ",Blist)
print("Extended Alist: ", Alist)

print("How many 5 is in the Blist: ",Blist.count(5))
print("The position of 5 in the Blist: ", Blist.index(5))

add = 0
for n in Blist:
    add += n
print("The lumpsum of Blist is: ",add)

print("My reversed list: ", Alist[::-1]) #This is extended slice syntax. It works by doing [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string.

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]) #listcomp combines the elements of two lists if they are not equal

