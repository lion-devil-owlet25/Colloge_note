class StringManipulation
{
public static void main(String args[])
{
StringBuffer str=new StringBuffer("Object language");
System.out.println("Original String:-"+str);
System.out.println("Length of String:-"+str.length());
for(int i=0;i<str.length();i++)
{
int pos=i+1;
System.out.println("Character at position "+pos+" is "+str.charAt(i));
}
String aString=new String(str.toString());
int pos=aString.indexOf("language");
str.insert(pos,"Oriented");
System.out.println("Modified String:"+str);
str.setCharAt(6,'-');
System.out.println("String now: "+str);
str.append("impoves security");
System.out.println("Appended String:"+str);
}
}
