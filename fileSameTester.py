file1 = open(input("file 1: "), "r")
file2 = open(input("file2: "), "r")

file1Conts = file1.read()
file2Conts = file2.read()
file1.close()
file2.close()

if(file1Conts == file2Conts):
    print("exact match")
else:
    print("not the same")
