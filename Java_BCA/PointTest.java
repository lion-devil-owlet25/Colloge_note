import java. util.*;
class Point
{
float xCo,yCo;
Point( ){xCo=0.0f; yCo=0.0f;}
Point(float x, float y){xCo=x; yCo=y;}
float getX( ){return xCo;}
float getY( ){return yCo;}
void setX(float val){xCo=val;}
void setY(float val){yCo=val;}
double getNorm(){return Math.sqrt( xCo*xCo + yCo*yCo);}
}
class PointTest
{
public static void main(String a[ ])
{
Point p1=new Point(3.0f,4.0f);
Point p2=new Point( );
System. out.println("The norm of the point(3,4) is"+p1.getNorm());
}
}