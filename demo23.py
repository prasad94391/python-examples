# exmaple program to read a file from current directory

#f = open("durga.txt","r")
#s = f.read()
#print(s)

#read only some characters

#f = open("durga.txt","r")
#s = f.read(30)
#print(s)

import os.path as pa
p = input("enter something:")
res = pa.exists(p)
if res:
    f = open(p)
    s = f.read()
    print(s)
else:
    print("file is not avalible")

