import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		// (1, 1)에서 시작하여 (n, n)으로 이동
		// 오른쪽 혹은 밑으로만 이동
		// dp[i][j] = max(dp[i][j-1], dp[i-1][j])
		// 거쳐간 위치에 적혀있는 숫자의 합을 최대로 하는 프로그램
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int[][] arr = new int[n][n];
		int[][] dp = new int[n][n];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < n; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		dp[0][0] = arr[0][0];
		// dp[1][0] = dp[0][0] + arr[1][0];
		// dp[2][0] = dp[1][0] + arr[2][0];
		// dp[0][1] = dp[0][0] + arr[0][1];
		// dp[0][2] = dp[0][1] + arr[0][2];

		for (int i = 1; i < n; i++) {
			dp[i][0] = dp[i-1][0] + arr[i][0];
		}
		
		for (int i = 1; i < n; i++) {
			dp[0][i] = dp[0][i-1] + arr[0][i];
		}

		for (int i = 1; i < n; i++) {
			for (int j = 1; j < n; j++) {
				dp[i][j] = Math.max(dp[i][j-1] + arr[i][j], dp[i-1][j] + arr[i][j]);
			}
		}

		System.out.println(dp[n-1][n-1]);
	}
}
