def isPalindorme(s):
    l=0
    r=len(s)-1
    while(r>=l):
        if s[l]==s[r]:
            l+=1
            r-=1
        else:
            return False
    return True
def main():
    m = 0
    for i in range(999,111,-1):
        for j in range(999,111,-1):
            if(isPalindorme(str(i*j))):
                m = max(i*j,m)
    return m

if __name__ =="__main__":
    print(main())
