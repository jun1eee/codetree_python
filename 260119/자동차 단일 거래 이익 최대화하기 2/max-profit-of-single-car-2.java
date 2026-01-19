import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        int[] arr1 = new int[n];
        int[] arr2 = new int[n];

        st = new StringTokenizer(br.readLine(), " ");

        for (int i = 0; i < n; i++) {
            arr1[i] = Integer.parseInt(st.nextToken());
        }

        // int max = Integer.MIN_VALUE;
        // boolean flag = false;

        // for (int i = 0; i < n-1; i++) {
        //     for (int j = i+1; j < n; j++) {
        //         if (arr[i] > arr[j]) {
        //             continue;
        //         } else {
        //             int profit = arr[j] - arr[i];

        //             if (profit > max) {
        //                 max = profit;
        //             }

        //             flag = true;
        //         }
        //     }
        // }

        // if (flag) {
        //     System.out.println(max);
        // } else {
        //     System.out.println(0);
        // }

        System.arraycopy(arr1, 0, arr2, 0, arr1.length);

        Arrays.sort(arr1);   // 2, 3, 6, 9, 10

        int max = Integer.MIN_VALUE;
        boolean flag = false;

        int profit = 0;

        for (int i = n-1; i >= 0; i--) {
            for (int j = 0; j < n; j++) {
                if (arr1[i] == arr2[j]) {
                    break;
                } else if (arr1[i] < arr2[j]) {
                    continue;
                } else {
                    profit = arr1[i] - arr2[j];
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