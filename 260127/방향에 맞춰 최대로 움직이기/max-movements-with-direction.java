import java.util.*;
import java.io.*;

public class Main {
    public static int n;
    public static int[][] arr;
    public static int[][] dir;
    public static int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
    public static int[] dy = {0, 1, 1, 1, 0, -1, -1, -1};
    public static int max = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        arr = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dir = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < n; j++) {
                dir[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine(), " ");
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        func(r-1, c-1, 0);

        System.out.println(max);
    }

    public static boolean check(int x, int y) {
        if (x >= 0 && x < n && y >= 0 && y < n) {
            return true;
        }

        return false;
    }

    public static void func(int startX, int startY, int count) {
        if (count > max) {
            max = count;
        }

        for (int i = 1; i <= n; i++) {
            int dirNum = dir[startX][startY];
            int nextX = startX + dx[dirNum - 1] * i;
            int nextY = startY + dy[dirNum - 1] * i;

            if (!check(nextX, nextY)) {
                break;
            }

            if (arr[nextX][nextY] > arr[startX][startY]) {
                func(nextX, nextY, count+1);
            }
        }
    }
}