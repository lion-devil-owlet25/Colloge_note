class Super
{
public void method()
{
System.out.println("Method Super");
}
}
class Sub extends Super
{
public void method()
{
System.out.println("Method Sub");
}
}
class dynamic_dispatch
{
public static void main(String args[])
{
Super A=new Sub();
A.method();
}
}
