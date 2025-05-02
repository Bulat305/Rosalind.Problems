n1=str(input())
n=n1[::-1]
#print(n)

for i in n:
    if i == "T":
        print("A", end='')
    if i == "A":
        print("T", end='')
    if i == "C":
        print("G", end='')
    if i == "G":
        print("C", end='')
