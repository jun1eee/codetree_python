import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine(), " ");

        int[] arr = new int[n];

        // 최장 감소 부분 수열의 길이 출력
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[n+1];

        // dp[n]: 길이가 n일때 감소하는 최대 부분 수열의 길이
        dp[1] = 1;
        
        for (int i = 1; i < n; i++) {
            if (arr[i-1] > arr[i]) {
                dp[i+1] = dp[i] + 1;
            } else {
                dp[i+1] = dp[i];
            }
        }

        System.out.println(dp[n]);
    }
}