#!/usr/bin/python3
import os
import argparse

## Is the Notification arg set? -n
parser = argparse.ArgumentParser(description="Rename audiobook with right numbers")
parser.add_argument("--inputpath", "-i", help="Input-path where audiobook is stored")
args = parser.parse_args()

def substringReplace(input, pattern, replacewith):
    return input.replace(pattern, replacewith)



if not os.path.isdir(args.inputpath):
    print("Not a valid path.")
    exit()
else:
    print("Using path "+args.inputpath)

usedPath = args.inputpath
if usedPath[len(usedPath)-1] != "/":
    print("Path missing terminal /")
    usedPath = usedPath + "/"
    print("Using " + usedPath)
filesInPath=[]
for root, dirs, files in os.walk(usedPath):
    for file in files:
        filesInPath.append(file)

#for name in filesInPath:
#    print(name)

#now we split the name of first file.
chunks = filesInPath[0].split(' ')
print("Old filenames: \n\nLINE --->  PART OF NAME")
for line in chunks:
    print(str(chunks.index(line)) + "    --->  "+ line)

print("Put the new name in. use %line for parts of the old name.")
newName = input()
prototype = newName
for chunk in reversed(chunks): ##do it other way round bcs %11 != &1 1 
    newName = substringReplace(newName, str("%" + str(chunks.index(chunk))), chunk )


print("The new name is going to be: " + newName + "\nThis will only work, if all files have the same name except for differing numbers etc.. \nIS THAT OK? -> type y/n")
ans = input()
if ans != "y":
    print("Thats not a yes. Terminating.")
    exit()

print("Renaming. Please Wait.")
for i in range(0, len(filesInPath)):
    #split name.
    parts = filesInPath[i].split(' ')
    #get our prototype
    newName = prototype
    for part in reversed(parts):
        newName = substringReplace(newName, str("%" + str(parts.index(part))), part  )
    #print(".", end="") #little progress
    os.rename(usedPath + filesInPath[i], usedPath + newName)
    print(filesInPath[i] + " --> " + newName)


print("\n\nDone. Have a nice day, sir or madame.")