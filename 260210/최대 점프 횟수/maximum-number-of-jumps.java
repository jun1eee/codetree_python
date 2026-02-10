import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        int[] arr = new int[n+1];

        st = new StringTokenizer(br.readLine(), " ");

        for (int i = 1; i <= n; i++) {
            // 각 위치로부터 최대 점프 가능의 거리
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // 시작 위치로부터 최대 몇 번 점프가 가능한지

        int[] dp = new int[n+1];  // dp[i]: 위치가 i번째일때 최대 점프 횟수

        dp[1] = 0;

        if (arr[1] > 0) {
            dp[2] = 1;
        }

        // 현재 위치 i
        for (int i = 3; i <= n; i++) {
            for (int j = 1; j <= i-1; j++) {
                if (j == 1) {
                    if (j + arr[j] >= i) {
                        dp[i] = Math.max(dp[i], dp[j] + 1);
                    }
                } else {
                    if (dp[j] > 0 && j + arr[j] >= i) {  // 비교 위치 + 최대 점프 가능 거리
                        dp[i] = Math.max(dp[i], dp[j] + 1);
                    }
                }
            }
        }

        int max = Integer.MIN_VALUE;

        for (int i = 1; i <= n; i++) {
            if (dp[i] > max) {
                max = dp[i];
            }
        }

        System.out.println(max);
    }
}