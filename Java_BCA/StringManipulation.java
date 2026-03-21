class StringManipulation 
{
     public static void main(String args[])
 {
   	StringBuffer str = new StringBuffer("Object language");
   	System.out.println("Original String :" + str);
   	// obtaining string length
        System.out.println("Length of string :" + str.length());
        // Accessing characters in a string
        for (int i = 0; i < str.length(); i++) 
	{
            int pos = i + 1;
            System.out.println("Character at position " + pos + " is " + str.charAt(i));
        }
        // Inserting a string in the middle
        String aString = new String(str.toString());
        int pos = aString.indexOf("language");
        str.insert(pos, "Oriented ");
        System.out.println("Modified string: " + str);
        // Modifying characters
        str.setCharAt(6, '-');
        System.out.println("String now: " + str);
        // Appending a string at the end
        str.append(" improves security.");
        System.out.println("Appended string: " + str);
    }
}
