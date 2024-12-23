def N_Times ():
    num=int (input())
    for i in range (num):
        n,c=input().split()
        n=int(n)
        print(" ".join(c*n))
N_Times()    

