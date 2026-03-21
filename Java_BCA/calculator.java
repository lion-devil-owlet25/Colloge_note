import java. util.Scanner;
class calculator
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
float a,b;
int lch;
System. out.println("Enter the number:-");
a=sc.nextFloat();
System. out.println("Enter the number:-");
b=sc.nextFloat();
System.out.println("Press 1 for addition");
System.out.println("Press 2 for subtraction");
System.out.println("Press 3 for multiplication");
System.out.println("Press 4 for division");
System.out.println("Enter your choice");
ch=sc.nextInt();
switch(ch)
{
case 1:
System. out.println("Addition:"+(a+b));
break;
case 2:
System. out.println("Subtraction:"+(a-b));
break;
case 3:
System. out.println("Multiplication:"+(a*b));
break;
case 4:
System. out.println("Division:"+(a/b));
break;
}
}
}




