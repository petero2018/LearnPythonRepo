import os

print(os.getcwd()) #current working directory
os.chdir("C:\Documents")
print(os.getcwd())
print(os.listdir(os.getcwd()))

if os.path.isdir("C:\Documents\Test") != True:
    os.mkdir("Test") #or os.makedirs("") create the path recursively

print(os.listdir(os.getcwd()))
if os.path.isdir("C:\Documents\Test") != True:
    os.rmdir("Test") #or os.removedirs("") removed intermediate directory rmdir doesn't

print(os.listdir(os.getcwd()))
if os.path.isdir("C:\Documents\Test\SubTest") != True:
    os.makedirs("Test/SubTest")

if os.path.isdir("C:\Documents\Test\SubTest") != True:
    os.rename("Test/SubTest","Test/SubTest_renamed")

print(os.listdir(os.getcwd()))
os.chdir("Test/SubTest_renamed")
print(os.stat("ftt_test.txt")) #print(os.path.exists("/home/el/myfile.txt"))

for dirpath, dirname, filename in os.walk("C:\Documents"):
    print("Current path:", dirpath)
    print("Directories:",dirname)
    print("Files:",filename)
    print()

print(os.path.join("C:\Documents", "Test")) #no guess work / is added
print(os.path.basename("C:\Documents\Test\SubTest_renamed/ftt_test.txt"))
print(os.path.dirname("C:\Documents\Test\SubTest_renamed/ftt_test.txt"))
print(os.path.split("C:\Documents\Test\SubTest_renamed/ftt_test.txt"))
print(os.path.exists("C:\Documents\Test\SubTest_renamed/ftt_test.txt"))
print(os.path.isfile("C:\Documents\Test\SubTest_renamed/ftt_test.txt"))
print(os.path.splitext("C:\Documents\Test\SubTest_renamed/ftt_test.txt"))
print(os.path.lexists("C:\Documents\Test\SubTest_renamed/ftt_test.txt"))

