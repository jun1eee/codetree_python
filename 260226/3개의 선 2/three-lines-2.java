import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        List<int[]> pointList = new ArrayList<>();

        int[][] visited = new int[n+1][n+1];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            pointList.add(new int[] {x, y});
        }

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

                if (temp1X == temp2X) {
                    xSet.add(temp1X);
                } else if (temp1Y == temp2Y) {
                    ySet.add(temp1Y);
                }
            }
        }

        if (xSet.size() + ySet.size() == 3) {
            System.out.println(1);
        } else if (xSet.size() + ySet.size() < 3) {
            System.out.println(0);
        }
    }
}