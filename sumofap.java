/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;
class A{
	
    static float sumOfAP(float n,float a,float d)
    {
        float sum;
        sum = (n / 2) * (2 * a + (n - 1) * d);
        int s=(int)sum;
        System.out.println(" "+s);
        return sum;
    } 
    
    public static void main(String args[])
    {
        float a,d,n;
        Scanner sc = new Scanner(System.in);
        n=sc.nextFloat();
        a=sc.nextFloat();
        d=sc.nextFloat();
        sumOfAP(n,a,d);
    }
    
}
        
    
        
