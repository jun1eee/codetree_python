import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int n = Integer.parseInt(st.nextToken());   // 서로 다른 동전 종류
        int k = Integer.parseInt(st.nextToken());   // 만들어야 하는 금액

        int[] coin = new int[n];

        // n개의 줄에 걸쳐 각 동전의 가치가 작은 동전부터 큰 동전까지 순서대로 주어짐
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            coin[i] = Integer.parseInt(st.nextToken());
        }

        int remain = k;
        int answer = 0;

        for (int i = n-1; i >= 0; i--) {
            int count = 0;

            while (remain - coin[i] >= 0) {
                remain -= coin[i];
                count++;
            }
            answer += count;
        }

        System.out.println(answer);
    }
}