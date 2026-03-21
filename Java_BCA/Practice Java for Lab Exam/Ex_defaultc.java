class perimeter
{
int length;
int breadth;
perimeter()
{
length=0;
breadth=0;
}
perimeter(int x, int y)
{
length=x;
breadth=y;
}
void cal_perimeter()
{
int peri;
peri=2*(length+breadth);
System.out.println("\n The perimeter of the rectangle is :- "+peri);
}
}
class Ex_defaultc
{
public static void main(String args[])
{
perimeter p1=new perimeter();
perimeter p2=new perimeter(5,10);
p1.cal_perimeter();
p2.cal_perimeter();
}
}
