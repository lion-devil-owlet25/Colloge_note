class Room
{
float length;
float breadth;
void getData(float a, float b)
{
length=a;
breadth=b;
}
}
class RoomArea
{
public static void main(String args[])
{
float area;
Room room=new Room();
room.getData(14,10);
area=room.length*room.breadth;
System.out.println("Area= "+area);
}
}
