import java.util.*;
import java.io.*;

public class Main {
    public static int n;
    public static int m;
    public static int[][] arr;
    public static boolean[][] visited;
    public static int[] dx = {-1, 0, 1, 0};
    public static int[] dy = {0, -1, 0, 1};

    public static void main(String[] args) throws IOException {
        // k 이하인 집들은 전부 물에 잠김
        // 안전 영역의 수가 최대가 되는 k와 그때의 안전 영역의 수 출력
        // k가 여러개라면 그 중 가장 작은 k 출력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n][m];

        int max = 0;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (arr[i][j] > max) {
                    max = arr[i][j];
                }
            }
        }

        int maxCount = 0;
        int maxK = 0;

        for (int k = 1; k <= max; k++) {
            int count = 0;
            visited = new boolean[n][m];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (arr[i][j] > k && !visited[i][j]) {
                        visited[i][j] = true;
                        dfs(i, j, k);
                        count++;
                    }
                }
            }

            if (count > maxCount) {
                maxCount = count;
                maxK = k;
            }
        }

        System.out.print(maxK + " " + maxCount);
    }

    public static void dfs(int x, int y, int k) {
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && arr[nx][ny] > k) {
                visited[nx][ny] = true;
                dfs(nx, ny, k);
            } 
        }
    }
}