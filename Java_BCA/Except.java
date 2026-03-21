import java. util.*;
public class Except1
{
public static void main(String[] args)
{
Scanner sc=new Scanner(System.in);
int a,b,c;
try
{
System. out.println("Enter number1:-");
a=sc.nextInt();
System. out.println("Enter number2:-");
b=sc.nextInt();
c=a/b;
System. out. println("c: "+c);
System. out.println("Welcome");
}
catch(ArithmeticException ex)
{
System. out.println("Error: "+ex.getMessage());
}
finally
{
System.out.println("Always executed");
}
}
}