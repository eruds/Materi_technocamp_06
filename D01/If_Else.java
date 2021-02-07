import java.util.Scanner;
public class If_Else {
    public static void main(String[] args) {
        // Creating a Scanner Object
        Scanner in = new Scanner(System.in); 

        // Conditional Example 1
        int x = 10; 
        int y = 10;
        if( x == y ){ 
            System.out.println("Var x (" + x + ") Is Equals to var y (" + y + ")");
        }

        // Conditional Example 2
        int A; 
        System.out.println("Tahun berapakah yang ingin Anda cek? : ");
        A = Integer.parseInt(in.nextLine());
        if (A % 4 == 0){ 
            if (A % 100 == 0){ 
                if (A % 400 == 0) {
                    System.out.println("Tahun tersebut merupakan tahun kabisat");
                } else {
                    System.out.println("Tahun tersebut bukan tahun kabisat");
                }}
            else {
                    System.out.println("Tahun tersebut merupakan tahun kabisat");
                }}
        else {
            System.out.println("Tahun tersebut bukan tahun kabisat");
        }
        in.close();
    }
}
