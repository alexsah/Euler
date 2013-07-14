public class Main {

    public static void main(String[] args) {
        for (int i = 1; i <500; i++) {
            for (int j = i+1; j<500; j++)     {
                double cValue = Math.sqrt(i*i + j*j);
                if ((cValue%1==0)&&(i+j+cValue)==1000)  {
                    System.out.println("a is " + i + ", b is " + (j) + ", c is " + cValue )  ;
                    System.out.println("Product is " + (int)(i * j * cValue));
                }
            }
        }
    }
}
