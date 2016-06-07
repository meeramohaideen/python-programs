n=int(input("Enter the size of an array"))
arr=[]
for i in range(0,n):
    v=int(input("Enter"))
    arr.append(v)
arr1=sorted(arr)
i=0
while (i<n):
	j=i+1
	while(j<n):
		if(arr1[i]==arr1[j]):
			print("%d is repeated.\n"%(arr1[i]))
			break
		j=j+1
	i=i+1
	
