n=str(input())
b= 0
gc = 0
print( n.count("A"), n.count("C"), n.count("G"), n.count("T"),)
# A», «C», «G» и «T»..
for i in n:
    b += 1
    if i == "G" or i == "C":
        gc +=1


    print(i)
    print(b)
    print(gc)
print((gc/b) * 100)