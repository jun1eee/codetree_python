import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 1 ~ 2N까지의 번호가 쓰인 카드
        // A와 B는 한 번에 카드 한 장씩을 내고, 더 큰 숫자의 카드를 가진 사람이 점수를 1점 얻는다.
        // A가 얻을 수 있는 점수의 최댓값
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        boolean[] used = new boolean[2*n+1];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            used[arr[i]] = true;
        }

        Arrays.sort(arr);

        // n이 3이면, 1~6까지 카드
        // 1, 6, 4
        // 2, 3, 5

        // 1, 4, 6
        // 2, 3, 5

        int answer = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 1; j <= 2*n; j++) {
                if (!used[j] && arr[i] < j) {
                    answer++;
                    used[j] = true;
                    break;
                }
            }
        }

        System.out.println(answer);
    }
}