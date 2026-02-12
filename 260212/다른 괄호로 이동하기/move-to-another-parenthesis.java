import java.util.*;
import java.io.*;

class Node implements Comparable<Node> {
    int nodeX;
    int nodeY;
    int time;

    Node(int nodeX, int nodeY, int time) {
        this.nodeX = nodeX;
        this.nodeY = nodeY;
        this.time = time;
    }

    @Override
    public int compareTo(Node node) {
        return this.time - node.time;
    }
}

public class Main {
    public static int n;
    public static int a;
    public static int b;
    public static String[] arr;
    public static int[][] dist;
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};
    public static int INF = (int)1e9;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        n = Integer.parseInt(st.nextToken());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());

        arr = new String[n];
        dist = new int[n][n];

        for (int i = 0; i < n; i++) {
            arr[i] = br.readLine();
        }

    

        // 인접한 칸 사이의 이동 가능
        // 대각선 방향으로의 이동 불가능
        // 이동 칸과 현재 칸의 기호가 같을 경우 A시간, 다를 경우 B시간

        // 모든 칸에 대해 임의로 출발칸과 도착칸을 정함
        // 이동시간이 최대가 되는 경우

        int max = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {

                for (int k = 0; k < n; k++) {
                    for (int l = 0; l < n; l++) {
                        dist[k][l] = INF;
                    }
                }

                dist[i][j] = 0;
                dijkstra(i, j);

                for (int k = 0; k < n; k++) {
                    for (int l = 0; l < n; l++) {
                        if (dist[k][l] != INF) {
                            if (dist[k][l] > max) {
                                max = dist[k][l];
                            }
                        }
                    }
                }
            }
        }

        System.out.println(max);
    }

    public static boolean check(int x, int y) {
        if (x >= 0 && x < n && y >= 0 && y < n) {
            return true;
        }

        return false;
    }

    public static void dijkstra(int startX, int startY) {
        PriorityQueue<Node> pq = new PriorityQueue<>();

        pq.add(new Node(startX, startY, 0));
        dist[startX][startY] = 0;

        while(!pq.isEmpty()) {
            Node curr = pq.poll();
            int currX = curr.nodeX;
            int currY = curr.nodeY;
            int time = curr.time;

            if (dist[currX][currY] != time) {
                continue;
            }

            for (int i = 0; i < 4; i++) {
                int nextX = currX + dx[i];
                int nextY = currY + dy[i];
                int moveTime;

                if (!check(nextX, nextY)) {
                    continue;
                }

                if (arr[currX].charAt(currY) == arr[nextX].charAt(nextY)) {
                    moveTime = a;
                } else {
                    moveTime = b;
                }

                if (dist[nextX][nextY] > dist[currX][currY] + moveTime) {
                    dist[nextX][nextY] = dist[currX][currY] + moveTime;
                    pq.add(new Node(nextX, nextY, dist[nextX][nextY]));
                }
            }
        }
    }
}