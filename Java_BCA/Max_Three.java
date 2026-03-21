import java.util.Scanner;
public class Max_Three 
{
    public static void main(String[] args) 
    {
        Scanner sc=new Scanner(System.in);
        int a,b,c;
        System.out.println("\n Enter the number");
        a=sc.nextInt();
        b=sc.nextInt();
        c=sc.nextInt();
        
        if(a>b && a>c)
        {
            System.out.println(a);
        }
        else if(b>c && b>a)
        {
            System.out.println(b);
        }
        else
        {
            System.out.println(c);
        }

    }
}
