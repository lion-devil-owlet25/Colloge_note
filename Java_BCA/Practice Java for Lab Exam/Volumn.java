import java.util.*;
class Volumn
{
public static void main(String args[])
{
Scanner sc= new Scanner(System.in);
int a,b,c;
System.out.println("Enter length:-");
a=sc.nextInt();
System.out.println("Enter breadth:-");
b=sc.nextInt();
System.out.println("Enter height:-");
c=sc.nextInt();
int area,volumn;
area=a*b;
volumn=a*b*c;
System.out.println("Area:-"+area);
System.out.println("Volumn:-"+volumn);
}
}