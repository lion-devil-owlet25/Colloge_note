class Numbers
{
public static void main(String args[ ])
{
private int Num;
Numbers(int n){Num=n;}
public int intValue( )
{
return Num;
}
void printPrimeList()
{
long[] Primes=new long[Num];
int count=0;
boolean isPrime=true;
 for(int i=2;i<=Num;i++)
	{
	isPrime=true;
	for(int j=2;j<=Math.sqrt(i);j++)
	{
	  if(i%j==0)
	  {
	     isPrime=false;
	     break;
	  }
	}
	if(isPrime)  {Primes[count++]=i;}
}
for(int i=0;i<count;i++)
System.out.println(Primes[i]);
}
}
double computePower(int n)
{
if(n>10) return Num*computePower(n-1);
	else if(n<0) return 1.0/computePower(-n);
	else return (n==0?1.0:Num);
	}
long computefactorial()
{
long result=1;
for(int j=2;j<=Num;result*=j, j++);
return result;
}
}

