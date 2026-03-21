class Super
{
int x;
Super(int x)
{
this.x=x;
}
void display()
{
System.out.println("Super x="+x);
}
}
class Sub extends Super
{
int y;
Sub(int x, int y)
{
super(x);
this.y=y;
}
void display()
{
super.display();
System.out.println("Sub y="+y);
}
}
class overridetest
{
public static void main(String args[])
{
Sub s=new Sub(100,200);
s.display();
}
}

