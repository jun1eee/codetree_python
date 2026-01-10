import java.util.*;
import java.io.*;

public class Main {
    public static int n;
    public static List<int[]> lineList;
    public static int count;
    public static int maxCount;
    public static List<int[]> answerLineList;

    public static void main(String[] args) throws IOException {
        // 수직선상에 N개의 선분
        // 서로 겹치지 않고 고를 수 있는 가장 많은 선분의 수 출력
        // 끝점을 공유하는 것도 겹친 것
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());

        lineList = new ArrayList<>();
        answerLineList = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");

            int l = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());

            lineList.add(new int[] {l, r});
        }

        Collections.sort(lineList, (a, b) -> {
            if (a[1] != b[1]) return a[1] - b[1];
            return a[0] - b[0];
        });

        func(0);

        System.out.println(maxCount);
    }

    public static void func(int num) {
        if (num == lineList.size()) {
            if (answerLineList.size() > maxCount) {
                maxCount = answerLineList.size();
            }

            return;
        }

        int start = lineList.get(num)[0];    // 시작점
        int end = lineList.get(num)[1];  // 끝점

        boolean flag = false;

        if (answerLineList.size() == 0) {
            answerLineList.add(new int[] {start, end});
            flag = true;
        } else {
            int priorStart = answerLineList.get(answerLineList.size() - 1)[0];
            int priorEnd = answerLineList.get(answerLineList.size() -1)[1];

            if (priorEnd < start) {
                answerLineList.add(new int[] {start, end});
                flag = true;
            }
        }

        func(num+1);

        if (flag) {
            answerLineList.remove(answerLineList.size() - 1);
        }

        func(num+1);
    }
}