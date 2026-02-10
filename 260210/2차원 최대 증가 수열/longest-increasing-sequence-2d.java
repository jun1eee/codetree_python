import java.util.*;
import java.io.*;

public class Main {
    public static int n;
    public static int m;
    public static int[][] arr;
    public static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n+1][m+1];    // (1, 1)에서 출발

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 1; j <= m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 점프 진행시 항상 현재 위치에 적혀있는 수보다, 
        // 점프한 이후의 칸에 적혀있는 수가 더 커야만 한다.

        // 점프 진행시 현재 위치에서 적어도 한칸 이상 오른쪽인 동사에 아래쪽에 있는 위치인 곳으로만 점프 가능

        // 밟을 수 있는 최대 칸의 수를 출력

        dp = new int[n+1][m+1];
        dp[1][1] = 1;

        func(1, 1);
        
        int max = Integer.MIN_VALUE;
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (dp[i][j] > max) {
                    max = dp[i][j];
                }
            }
        }

        System.out.println(max);
    }

    public static boolean check(int x, int y) {
        if (x >= 1 && x <= n && y >= 1 && y <= n) {
            return true;
        }

        return false;
    }

    public static void func(int startX, int startY) {

        for (int i = 1; startX + i <= n; i++) {
            for (int j = 1; startY + j <= n; j++) {
                int nextX = startX + i;
                int nextY = startY + j;

                if (check(nextX, nextY)) {
                    if (arr[startX][startY] < arr[nextX][nextY]) {
                        dp[nextX][nextY] = Math.max(dp[nextX][nextY], dp[startX][startY] + 1);
                        func(nextX, nextY);
                    }
                }
            }
        }
    }
}