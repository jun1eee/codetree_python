import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int count = 0;
        boolean flag = false;
        boolean zeroFlag = false;

        while (true) {
            n -= 2;
            count++;

            if (n < 0) {
                flag = true;
                break;
            }

            if (n % 5 == 0) {
                break;
            }

            if (n == 0) {
                zeroFlag = true;
                break;
            }
        }

        if (flag) {
            System.out.println(-1);
            return;
        }

        if (zeroFlag) {
            System.out.println(count);
            return;
        }

        while (true) {
            n -= 5;
            count++;

            if (n == 0) {
                break;
            }
        }

        if (n == 0) {
            System.out.println(count);
        } else if (n < 0) {
            System.out.println(-1);
        }
    }
}