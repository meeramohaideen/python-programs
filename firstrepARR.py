n=int(input("Enter the size of an array"))
arr=[]
for i in range(0,n):
    v=int(input("Enter"))
    arr.append(v)
#arr1=sorted(arr)
print(arr)
i=0
while (i<n):
	j=i+1
	while(j<n):
		if(arr[i]==arr[j]):
			print(arr[i])
			q='Q'
		j=j+1
	i=i+1
	if(q=='Q'):
		break
