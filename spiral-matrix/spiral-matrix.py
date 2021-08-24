n=int(input())
a=n*2-1

c=0
b = [[0 for j in range(n)] for i in range(n)]
z=1
if n%2!=0:
    for p in range (0,a//4):
        for i in range (p,n-p):  #p1=0 k1=n  p in range
            b[p][i]=z
            z+=1
        c+=1
        for j in range (p+1,n-p): #p2=1 k2=n
            b[j][n-1-p]=z
            z+=1
        c+=1
        for i in range (n-2-p,p-1,-1): #p3=n-2  k3=-1
            b[n-1-p][i]=z
            z+=1
        c+=1
        for j in range (n-2-p,p,-1):  #p4=n-2   k4=0
            b[j][p]=z
            z+=1
        c+=1

    b[n//2][n//2]=z
    z+=1
    c+=1
#print (c)

else:
   for p in range (0,a//4):
        for i in range (p,n-p):
            #p1=0 k1=n  p in range
            b[p][i]=z
            z+=1

        c+=1
        for j in range (p+1,n-p): #p2=1 k2=n
            b[j][n-1-p]=z
            z+=1
        c+=1
        for i in range (n-2-p,p-1,-1): #p3=n-2  k3=-1
            b[n-1-p][i]=z
            z+=1
        c+=1
        for j in range (n-2-p,p,-1):  #p4=n-2   k4=0
            b[j][p]=z
            z+=1
        c+=1
#last four values

   b[n//2-1][n//2-1]=z
   z+=1
   c+=1

   b[n//2-1][n//2]=z
   z+=1
   c+=1

   b[n//2][n//2]=z
   z+=1
   c+=1

   b[n//2][n//2-1]=z
   z+=1
   c+=1


for k in range (n):
    for m in range (n):
        print (b[k][m],end=' ')
    print()
