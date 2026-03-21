class Multable
{
final static int r=20;
final static int c=20;
public static void main(String args[ ])
{
int product[][]=new int[r][c];
System.out.println("Multiplication table");
System.out.println(" ");
int i,j;
for(i=10;i<r;i++)
{
	for(j=10;j<c;j++)
	{
	product[i][j]=i*j;
	System.out.print(" "+product[i][j]);
	}
System.out.println(" ");
}
}
}