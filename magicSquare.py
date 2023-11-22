def magic_square(n):
 
    magic_square=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magic_square.append(l)

#     for i in range(n):
#         for j in range(n):
#             print(magic_square[i][j],end=" ")
#         print()
# magic_square(3)


    i=n//2
    j=n-1
    num=n*n
    count=1
    while(count<=num):
        if(i==-1 and j==n):
            j=n-2
            i=0
        else:
            if(j==n):
                j=0
        if (magic_square[i][j]!=0):
            j=j-2
            i=i+1
            continue
        else:
            magic_square[i][j]=count
            count+=1

        i=i-1
        j=j+1
    for i in range(n):
        for j in range(n):
            print(magic_square[i][j],end=" ")
        print()
    print("The sum of each row/column/diagonal is: "+str(n*(n**2+1)/2))

magic_square(3)