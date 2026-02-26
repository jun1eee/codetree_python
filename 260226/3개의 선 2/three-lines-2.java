import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        List<int[]> pointList = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            pointList.add(new int[] {x, y});
        }

        boolean[] visited = new boolean[n];

        Set<Integer> xSet = new HashSet<>();
        Set<Integer> ySet = new HashSet<>();

        for (int i = 0; i < n-1; i++) {
            int[] temp1 = pointList.get(i);
            int temp1X = temp1[0];
            int temp1Y = temp1[1];

            for (int j = i+1; j < n; j++) {
                int[] temp2 = pointList.get(j);
                int temp2X = temp2[0];
                int temp2Y = temp2[1];

                if (!visited[j] && temp1X == temp2X) {
                    visited[i] = true;
                    visited[j] = true;
                    xSet.add(temp1X);
                }

                if (check(n, visited) && xSet.size() == 3) {
                    System.out.println(1);
                    return;
                }
            }
        }

        for (int i = 0; i < n-1; i++) {
            int[] temp1 = pointList.get(i);
            int temp1X = temp1[0];
            int temp1Y = temp1[1];

            for (int j = i+1; j < n; j++) {
                int[] temp2 = pointList.get(j);
                int temp2X = temp2[0];
                int temp2Y = temp2[1];

                if (!visited[j] && temp1Y == temp2Y) {
                    visited[i] = true;
                    visited[j] = true;
                    ySet.add(temp1Y);
                }

                if (check(n, visited) && xSet.size() + ySet.size() == 3) {
                    System.out.println(1);
                    return;
                }
            }
        }

    
        System.out.println(0);
    }

    public static boolean check(int n, boolean[] visited) {
        for (int i = 0; i < n; i++) {
            if (visited[i] == false) {
                return false;
            }
        }

        return true;
    }
}