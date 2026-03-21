public class Except2
{
public static void main(String[]args)
{
try
{
int a[]={42,45,67,78};
a[10]=100;
for(int i=0;i<a.length;i++)
{
System.out.println(a[i]);
}
}
catch(ArrayIndexOutOfBoundsException ex)
{
System.out.println("Error: "+ex.getMessage());
}
finally
{
System.out.println("Always executed");
}
}
}

//output will be
// Error: Index 10 out of bounds for length 4
//Always executed