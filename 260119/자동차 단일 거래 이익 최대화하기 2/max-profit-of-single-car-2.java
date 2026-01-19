import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];

        st = new StringTokenizer(br.readLine(), " ");

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int max = Integer.MIN_VALUE;
        boolean flag = false;

        for (int i = 0; i < n-1; i++) {
            for (int j = i+1; j < n; j++) {
                if (arr[i] > arr[j]) {
                    continue;
                } else {
                    int profit = arr[j] - arr[i];

                    if (profit > max) {
                        max = profit;
                    }

                    flag = true;
                }
            }
        }

        if (flag) {
            System.out.println(max);
        } else {
            System.out.println(0);
        }
    }
}