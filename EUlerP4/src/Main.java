import java.io.*;

public class Main  {
    public static void main(String [] args){
        int greatestPalindrome = 0;
            BufferedReader object = new BufferedReader(
                    new InputStreamReader(System.in));
            System.out.println("Enter number");

            //int num= Integer.parseInt(object.readLine());
            int num = 999*998;
            for(int i=999; i>99; i--){
                for(int j=999; j>99; j--){
                    if (IsPalindrome(i,j) > greatestPalindrome)
                        greatestPalindrome = i*j;
                }
            }
        System.out.println("greatest palindrome found was " + greatestPalindrome);
    }

    public static int IsPalindrome(int j, int k)  {
        int num = j*k;
        //System.out.println(j + "x"+k);
        int n = num;
        int rev;
        rev = 0;
        //System.out.println("Number: ");
        //System.out.println(" "+ num);
        for (int i=0; i<=num; i++){
            int r=num%10;
            num=num/10;
            rev=rev*10+r;
            i=0;
        }

        if(n == rev){
            System.out.println("Number " + n + " is palindrome!");
            System.out.println("Product of " + j + " and " + k)   ;
            return n;
        }
        else{
            //System.out.println("Number " + n + " is not palindrome!");
            return 0;
        }

    }
}