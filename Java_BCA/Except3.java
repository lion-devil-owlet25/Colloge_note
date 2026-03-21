public class Except3
{
static Integer x;
public static void main(String[]args)
{
try
{
show(x);
}
catch(NullPointerException ex)
{
System.out.println("Error: "+ex.getMessage());
}
}
static void show(int a)
{
int p=a*2;
System. out. println("p: "+p);
}
}
