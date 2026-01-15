#include <stdio.h>
int main() 
{
int n,org, rev = 0, rem;
printf("Enter a number: ");
scanf("%d", &n);
org = n;
while (n != 0) 
{
    rem = n % 10;           
    rev = rev * 10 + rem; 
    n /= 10;                   
}
if (org == rev)
 {
    printf("%d is a Palindrome number.\n", org);
}
else
{
    printf("%d is not a Palindrome number.\n", org);
}
	return 0;
}

