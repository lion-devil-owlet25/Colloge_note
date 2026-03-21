import java.util.*;
class Ferenhite_to_Centigate
{
    public static void main(String args[])
   {
       Scanner sc=new Scanner(System.in);
       double C, F;
       System.out.print("Enter the Ferenhite:-");
       F=sc.nextDouble();
       C=(F-32)/1.8;
       System.out.print("Centigate:-"+C);
   }
}