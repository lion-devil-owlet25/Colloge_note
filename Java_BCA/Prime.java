import java. util.Scanner;
class Prime
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
int n, i,c=0;
System. out.println("Enter a number:-");
n=sc.nextInt();
for(i=2;i<n;i++)
{
if(n%i==0)
{
c=1;
break;
}
}
if(c==0)
System. out.println(n+" is a Prime Number");
else
System. out.println(n+" is not Prime Number");
}
}
