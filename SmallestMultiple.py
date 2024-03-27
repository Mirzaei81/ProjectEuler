import sys
end=2432902008176640000
for n in range(1,end):
    breaked =False
    for i in range(1,21) :
        if n%i!=0:
            breaked = True
            break
    if not breaked:
        print(n)
        sys.exit(0)

