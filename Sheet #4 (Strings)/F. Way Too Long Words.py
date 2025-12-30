num = int (input())   
for i in range(num+14
) :
    s=input()
    if len(s)<=10 :
        print(s)
    else :
        print(s[0]+str(len(s[1:-1]))+s[-1])
