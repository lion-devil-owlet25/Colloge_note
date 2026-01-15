#include <stdio.h>
int main() 
{
int n, i, num, sum;
printf("Enter size of array: ");
scanf("%d", &n);
int a[n];
printf("Enter %d numbers:\n", n);
for (i = 0; i < n; i++)
    scanf("%d", &a[i]);
for (i = 0; i < n; i++) 
{
    num = a[i];
    sum = 0;
	while (num) 
	{
    sum += num % 10;
    num /= 10;
    }
	printf("Sum of digits of %d = %d\n", a[i], sum);
    }
return 0;
}

