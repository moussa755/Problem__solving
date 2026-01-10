a,b=map(int,input().split())
arr = list(map(int, input().split()))
for  i in range (0,a,b) :
    num =arr[i:i+b]
    print(min(num))


