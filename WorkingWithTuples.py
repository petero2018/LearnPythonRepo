T = (1, 2, 3, 4)

print("Index 4 of my touple: ",T.index(4)) # Tuple methods: 4 appears at offset 3
print("Count of 4 in my touple: ",T.count(4)) # 4 appears once
print("My concatenated touple: ",T + (5, 6)) # Concatenation
T = (2,) + T[1:]  # Make a new tuple for a new value
print("New touple:",T)
T = 'spam', 3.0, [11, 22, 33]
print(T)

tup = ('physics', 'chemistry', 1997, 2000);
print(tup)
del tup;


print(3 in (1, 2, 3))