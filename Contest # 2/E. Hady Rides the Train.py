a = int (input())
arr = [[0,1,2,3],
       [7,6,5,4],     
       [8,9,10,11],
       [15,14,13,12],
       [16,17,18,19]]
for i in range (len(arr)):
 for j in range (len(arr[i])):
       if arr [i][j]==a:
        print (i ,j)

              
