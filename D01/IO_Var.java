import java.util.Scanner;

public class IO_Var {
    public static void main(String[] args) {
        // Creating a scanner object 
        Scanner in = new Scanner(System.in); 

        // Prompting an Input 
        String s = in.nextLine(); 
        System.out.println("You entered string "+s); 

        // Variable declaration 
        String a = "Hello"; 
        String b = "World"; 
        System.out.println(a + b); 

        int num1 = 20; 
        int num2 = 10; 
        System.out.println(num1 + num2);
        System.out.println(num1 >= num2); 
        in.close();
    }
}