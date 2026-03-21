import java. util.Scanner;
class factorial
{
public static void main(String args[])
{
int n, i,f=1;
Scanner sc = new Scanner(System.in);
System.out.println("Enter a number:-");
n=sc.nextInt();
for(i=n;i>=1;i--)
{
f=f*i;
}
System.out.print("Factorial of " + n + "="+ f);
}
}