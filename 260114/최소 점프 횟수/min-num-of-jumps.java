import java.util.*;
import java.io.*;

public class Main {
    public static int n;
    public static int[] maxJump;
    public static int min = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine(), " ");
        maxJump = new int[n];

        // 각 위치로부터의 최대 점프 가능 거리
        for (int i = 0; i < n; i++) {
            maxJump[i] = Integer.parseInt(st.nextToken());
        }

        func(0, 0);

        if (min == Integer.MAX_VALUE) {
            System.out.println(-1);
            return;
        }

        System.out.println(min);
    }

    public static void func(int start, int count) {
        // 최소 점프 횟수
        if (start == n-1) {
            if (count < min) {
                min = count;
            }
            return;
        }

        for (int i = 1; i <= maxJump[start]; i++) {
            int place = start + i; // 점프하고 난 후의 좌표
            func(place, count+1);
        }
    }
}