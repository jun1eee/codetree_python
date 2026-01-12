import java.util.*;
import java.io.*;

public class Main {
    public static int n;
    public static int[] arr;
    public static int[] dp;

    public static void main(String[] args) throws IOException {
        // n개의 숫자가 주어졌을 때 가장 긴 증가 부분 수열의 길이를 구하는 프로그램

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());

        arr = new int[n+1];
        dp = new int[n+1];

        st = new StringTokenizer(br.readLine(), " ");

        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // 9가 마지막 일 떄 6, 3, 1
        // 1, 6, 4, 3, 9, 3
        // dp[i] = dp[j] + 

        // dp[n]: n개의 숫자가 주어졌을 떄 가장 긴 증가 부분 수열의 길이

        dp[0] = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        int answer = 0;

        for (int i = 0; i <= n; i++) {
            if (dp[i] > answer) {
                answer = dp[i];
            }
        }

        System.out.println(answer);
    }
}