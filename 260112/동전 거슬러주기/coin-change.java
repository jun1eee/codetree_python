import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int n = Integer.parseInt(st.nextToken());   // n개의 동전의 종류
        int m = Integer.parseInt(st.nextToken());   // 금액 m

        // 금액 m을 거슬러주기 위해 필요한 최소 동전의 수

        st = new StringTokenizer(br.readLine(), " ");

        int[] arr = new int[n+1];
        int[] dp = new int[m+1];  //해당 금액을 거슬러주기 위해 필요한 최소 동전의 수

        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= m; i++) {
            dp[i] = Integer.MAX_VALUE;
        }

        dp[0] = 0;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (i >= arr[j]) {
                    if (dp[i-arr[j]] == Integer.MAX_VALUE) {
                        continue;
                    }

                    dp[i] = Math.min(dp[i], dp[i-arr[j]]+1);
                }
            }
        }

        int answer = dp[m];

        if (answer == Integer.MAX_VALUE) {
            answer = -1;
        }
        
        System.out.println(answer);
	}
}
