import java.util.Scanner;

public class Main {

    static String[] l = new String[1000000];
    static int n = 1;
    

    public static String solve(int i) {
        if (i >= n) {
            return "Yes'";
        }
        if (Float.parseFloat(l[i]) < 0) {
            return solve(i + 1);
        } else {
            return "No";
        }
    }

    public static void output(String n) {
        System.out.println(n);
    }

    public static void input() {
     Scanner scanner = new Scanner(System.in);
        n = Integer.parseInt(scanner.nextLine());
        l = scanner.nextLine().trim().split(" ");
    }

    public static void main(String[] args) {
       
Scanner scanner = new Scanner(System.in);
        int testcase = Integer.parseInt(scanner.nextLine());
        
        for (int i = 0; i < testcase; i++) {
            String n = solve(0);
            output(n);
            
        }
        
    }
}
