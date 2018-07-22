
f = open("test.txt",'r')
print("The name of my file: ",f.name)
f.close()
print("Is my file closed? ",f.closed)

print("write 20 lines to my file")
with open("test.txt",'w') as f:
    for fw in range(1,21):
        f.write(str(fw) + ') line \n ')

print("Read and print out all contents of my file")
with open("test.txt",'r') as f:
    f_contents = f.readline()
    print(f_contents, end='')

print("Read and print out first 100 characters of my file")
with open("test.txt",'r') as f:             #r -> read, w--> write, a--> append
    f_contents = f.read(100) #firt 100 characters
    print(f_contents, end='')

print("Read and print out all contents of my file by 100 character at the time")
with open("test.txt",'r') as f:
    size_to_load = 100
    f_contents = f.read(size_to_load)

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_load)

print("Read and print out the first 10 characters then re-position to the beginning of the file and print out another 10 characters")
with open("test.txt",'r') as f:
    size_to_load = 10
    f_contents = f.read(size_to_load)
    print(f_contents, end='')

    f.seek(0)

    f_contents = f.read(size_to_load)
    print(f_contents, end='')

print("Copy my file")
with open("test.txt",'r') as rf:
    with open("test_copy.txt", 'w') as wf:
        for line in rf:
            wf.write(line)

print("Copy my binary file")
with open("DL.jpg",'rb') as rf:
    with open("DL_copy.jpg", 'wb') as wf:
        for line in rf:
            wf.write(line)












