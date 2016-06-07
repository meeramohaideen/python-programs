arr=[]
n=int(input("Enter the size"))
print("the numbers should be unique")
for i in range(0,n):
	v=int(input())
	arr.append(v)
arr1=sorted(arr)
print(arr1)
for i in range(0,n):
	if(i==arr1[i]):
		print("the number %d equal its index %d"%(i,arr1[i]))
