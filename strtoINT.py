#include<stdio.h> 
 #include<stdlib.h> 
 #include<string.h>
 int main() 
 { 
 int i,n; 
 char str[123]; 
printf("enter the string"); 
scanf("%s",str);
n=strlen(str);
for(i=0;i<n;i++)
{
    printf("\n%c sfter conversion %d",str[i],str[i]);
}
 return 0; 
} 
