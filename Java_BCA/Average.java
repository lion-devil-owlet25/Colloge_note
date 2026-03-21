import java. util.*;
class Average
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
double a,b,c,avg;
System.out.print("Enter the number:-");
a=sc.nextDouble();
System.out.print("Enter the number:-");
b=sc.nextDouble();
System.out.print("Enter the number:-");
c=sc.nextDouble();
avg=(a+b+c)/3;
System.out.print("The average of 3 numbers :-"+avg);
}
}