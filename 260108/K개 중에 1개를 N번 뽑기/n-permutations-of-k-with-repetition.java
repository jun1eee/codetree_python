import java.util.*;
import java.io.*;

public class Main {
    public static int k;
    public static int n;
    public static List<Integer> list = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        // 1이상 K이하의 숫자를 하나 고르는 행위를 N번 반복

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        k = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        func(0);
    }

    public static void func(int length) {
        if (length == n) {
            for (int i = 0; i < n; i++) {
                System.out.print(list.get(i) + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 1; i <= k; i++) {
            list.add(i);
            func(length+1);
            list.remove(list.size()-1);
        }
    }
}