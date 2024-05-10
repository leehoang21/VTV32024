import java.util.Scanner;

public class Main {

    public static int solve(int i, String[] arr) {
        if (i < 0) {
            return 0;
        }
        if (arr[i].charAt(0) == '-') {
            return solve(i - 1, arr);
        } else {
            return 1 + solve(i - 1, arr);
        }
    }

    public static void output(int n) {
        System.out.println(n);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int testcase = Integer.parseInt(scanner.nextLine());
        String[] arr = scanner.nextLine().trim().split(" ");
        int n = solve(testcase - 1, arr);
        output(n);

        scanner.close();
    }
}
