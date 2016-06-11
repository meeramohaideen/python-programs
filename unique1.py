n=int(input("Enter the size of an array"))
arr=[]
for i in range(0,n):
    v=int(input("Enter"))
    arr.append(v)
arr1=sorted(arr)
#print(arr1)
i=0
while (i<n):
	j=i+1
	while(j<n):
		if(arr1[i]==arr1[j]):
			arr1[i]=0
			arr1[i+1]=0
			break
		j=j+1
	i=i+1
print(arr1)
for i in range(0,n):
	if(arr1[i]!=0):
		print("%d is unique"%(arr1[i]))
